## ⚠️ Disclaimer
This project is for **educational and ethical cybersecurity research only**. Do not use it for unauthorized tracking, phishing, or malicious activities. Unauthorized use of email tracking can violate privacy laws and terms of service.

📜 Legal & Ethical Guidelines

Ensure you have consent before sending tracking emails.

Do not impersonate organizations or individuals.

Comply with Mailjet’s policies and applicable privacy laws.

This tool should be used for internal security training, research, or authorized testing only.

## 📌 Overview
This Python script automates email sending using **Mailjet API** and **Canary Tokens** to track when recipients interact with the email. It is designed for **cybersecurity awareness, phishing simulation, and security research**.

## 🚀 Features
- Sends emails using **Mailjet API** from a verified sender.
- Uses **Canary Tokens** to track when a recipient clicks on the embedded link.
- Reads recipient emails from an **Excel (.xlsx) file**.
- Supports both **HTML and plain text email formats**.

## 🛠 Setup & Installation
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install requests pandas
```

### 2️⃣ Configure the Script
- Update the **Mailjet API Key** and **Secret Key** in the script.
- Modify the **Sender Email** to a verified email in Mailjet.
- Replace the **Canary Token Link** with your generated Canary Token.
- Ensure your **mails.xlsx** file contains a column named `Email` with recipient addresses.

### 3️⃣ Run the Script
Execute the script using:
```sh
python send_mails.py
```

## 📊 Usage
1. The script reads recipient emails from `mails.xlsx`.
2. Sends an email with the tracking link (Canary Token).
3. When a recipient clicks the link, **Canary Tokens will log the interaction**.




📌 Notes:
The emails are sent from your Mailjet account. Ensure your sender email is verified.
Use responsibly for authorized bulk email sending.
