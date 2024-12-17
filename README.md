# 🌪️ DisasterAlertMailer 📧

DisasterAlertMailer is a Python-based application that tracks weather alerts and sends emergency notifications via email. It uses the [WeatherAPI](https://www.weatherapi.com/) to fetch weather alerts and the [Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com) to send emails. The device's location is determined using the `ipinfo.io` service.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](https://github.com/aloukikjoshi/DisasterAlertMailer/edit/main/README.md#%EF%B8%8F-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 🌍 **Location Tracking**: Automatically tracks the device's location using `ipinfo.io`.
- 🌦️ **Disaster Alerts**: Fetches alerts from [WeatherAPI](https://www.weatherapi.com/).
- 📧 **Email Notifications**: Sends emergency alerts via Gmail.
- ⏰ **Scheduler**: Checks for disasters every 15 minutes (adjustable).

## 🛠️ Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/DisasterAlertMailer.git
    cd DisasterAlertMailer
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```dotenv
    FROM_EMAIL=your-email@gmail.com
    TO_EMAIL=recipient-email@gmail.com
    WEATHERAPI_KEY=your-weatherapi-key
    CLIENT_SECRET_FILE=client_secret.json
    ```

5. **Add your Google OAuth2 credentials**:
    Download your `client_secret.json` from the Google Cloud Console and place it in the root directory.

## ⚙️ Configuration

- **FROM_EMAIL**: The email address from which alerts will be sent.
- **TO_EMAIL**: The recipient email address for alerts.
- **WEATHERAPI_KEY**: Your API key for WeatherAPI.
- **CLIENT_SECRET_FILE**: The path to your Google OAuth2 client secret file.

## 🚀 Usage

1. **Run the application**:
    ```sh
    python dm.py
    ```

2. The application will start and check for weather alerts every 15 minutes. If an alert is found, an email will be sent to the specified recipient.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Aloukik Joshi](https://github.com/aloukikjoshi)
