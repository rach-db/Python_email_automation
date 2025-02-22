## ⚠️ Disclaimer
This project is for **educational and ethical cybersecurity research only**. Do not use it for unauthorized tracking, phishing, or malicious activities. Unauthorized use of email tracking can violate privacy laws and terms of service.

📜 Legal & Ethical Guidelines

Ensure you have consent before sending tracking emails.

Do not impersonate organizations or individuals.

Comply with Mailjet’s policies and applicable privacy laws.

This tool should be used for internal security training, research, or authorized testing only.

Bulk Email Sending Script with Canary Tokens

## Overview

This project contains a Python script designed to send bulk emails using Gmail's SMTP server. The emails contain a security update link generated via Canary Tokens for tracking purposes. The recipient list is managed through an Excel file.

## Features

Sends personalized emails to multiple recipients.

Uses Canary Token links for security tracking.

Reads email addresses and names from an Excel (.xlsx) file.

Uses Gmail's secure SMTP server for sending emails.

## Prerequisites

Python 3.x installed

Pandas library (pip install pandas)

openpyxl library (pip install openpyxl)

## Setup Instructions

  1.Clone the repository:

  git clone https://github.com/yourusername/your-repo-name.git
  cd your-repo-name

  2.Install dependencies:

  pip install pandas openpyxl

  3.Prepare your mails.xlsx file:
  Ensure your Excel sheet contains columns named Email and Name.

  4.Configure Gmail App Password:

  Enable 2-Step Verification on your Gmail account.

  Generate an App Password and use it in the script.

  5.Edit the script:
  Replace the following placeholders in the script:

  sender_email: Your Gmail address

  app_password: Your Gmail App Password

  canary_link: Your unique Canary Token link

## Running the Script

Execute the script using:

python send_mails.py

Notes

Emails might land in the spam folder — adjust the content and subject line for better deliverability.

Ensure the Canary Token link is correctly generated and active.

## 📊 Usage
1. The script reads recipient emails from `mails.xlsx`.
2. Sends an email with the tracking link (Canary Token).
3. When a recipient clicks the link, **Canary Tokens will log the interaction**.


📌 Notes:
Use responsibly for authorized bulk email sending.
