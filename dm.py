import base64
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import schedule
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()
print("Environment variables loaded")

# Define the SCOPES variable
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Function to send email using OAuth2
def send_email(to_email, subject, body):
    print("send_email function called")
    from_email = os.getenv("FROM_EMAIL")
    creds = None

    # Check if token.json exists for authentication
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If credentials are not valid, initiate OAuth2 flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.getenv("CLIENT_SECRET_FILE"), SCOPES
            )
            creds = flow.run_local_server(port=8888)  # Explicitly set redirect_uri port

        # Save the credentials for the next time
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=creds)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Encode the message to base64
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw_message}

    # Send the email using Gmail API
    service.users().messages().send(userId='me', body=message).execute()
    print(f"Email sent to {to_email}")


# Function to fetch weather alerts using WeatherAPI
def get_weather_alerts(api_key, location):
    print("get_weather_alerts function called")
    url = f"https://api.weatherapi.com/v1/alerts.json?key={api_key}&q={location}"
    response = requests.get(url)

    # Check if response is valid
    if response.status_code != 200:
        print(f"Error fetching weather data: {response.status_code}")
        return []

    data = response.json()
    if 'alerts' in data and 'alert' in data['alerts']:
        return data['alerts']['alert']
    else:
        return []


# Function to check for disasters and send alerts
def check_for_disasters():
    print("check_for_disasters function called")
    location = os.getenv("LOCATION")
    api_key = os.getenv("WEATHERAPI_KEY")
    if not location or not api_key:
        print("Error: Missing LOCATION or WEATHERAPI_KEY in environment variables")
        return

    print(f"Checking for disasters in {location}")
    alerts = get_weather_alerts(api_key, location)

    if alerts:
        for alert in alerts:
            print(f"Alert found: {alert['headline']}")
            send_email(os.getenv("TO_EMAIL"), "Emergency Alert", alert['headline'])
    else:
        print("No alerts found")


# Schedule the task to run every 15 minutes (adjustable)
schedule.every(1).minutes.do(check_for_disasters)
print("Scheduler started")

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(10)
