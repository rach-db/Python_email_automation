
⚠️ Disclaimer: This project is for educational and ethical use only. Do not use it for unauthorized tracking.

# 📧 Email Sender Script

This is a Python script for sending bulk emails using the **Mailjet API** and an Excel email list.  

## 🚀 Features:
- Sends emails in bulk using an Excel file (`mails.xlsx`).
- Supports **HTML email content**.
- Uses **Mailjet API** for sending emails securely.
- Customizable email subject and body.

## 🛠️ Requirements:
- Python 3.x
- `requests` and `pandas` libraries
- A verified **Mailjet** account with API keys

## 🔧 Setup Instructions:
1. Clone this repository:
   ```sh
   git clone https://github.com/rach-db/repository-name.git
   cd repository-name
2. Install required libraries:
    pip install requests pandas openpyxl
3. Update MAILJET_API_KEY and MAILJET_SECRET_KEY in send_mails.py.
4. Run the script:
   python send_mails.py

📌 Notes:
The emails are sent from your Mailjet account. Ensure your sender email is verified.
Use responsibly for authorized bulk email sending.
