import requests
import pandas as pd

# Mailjet API Credentials
MAILJET_API_KEY = "your-mailjet-api-key"
MAILJET_SECRET_KEY = "your-mailjet-secret-key"

# Your sender email (must be verified in Mailjet)
SENDER_EMAIL = "your-email"

# Your Canary Token tracking link
CANARY_TOKEN_LINK = "https://your-canary-token-link.com"
# Load email list from an Excel file
email_list = pd.read_excel("mails.xlsx")  # Ensure this file has a column 'Email'

# Mailjet API Endpoint
MAILJET_URL = "https://api.mailjet.com/v3.1/send"

for index, row in email_list.iterrows():
    recipient_email = row['Email']

    data = {
        "Messages": [
            {
                "From": {"Email": SENDER_EMAIL, "Name": "IT Support Team"},
                "To": [{"Email": recipient_email}],
                "Subject": "Action Required: Verify Your Access",
                "TextPart": (
                    "Hello,\n\n"
                    "We need a quick confirmation from you regarding your recent login activity. "
                    "Please check the following link and confirm your details:\n\n"
                    f"{CANARY_TOKEN_LINK}\n\n"
                    "Let us know if you have any concerns.\n\n"
                    "Best,\n"
                    "IT Support Team"
                ),
                "HTMLPart": (
                    "<p>Hello,</p>"
                    "<p>We need a quick confirmation regarding your recent login activity.</p>"
                    f"<p>Please <a href='{CANARY_TOKEN_LINK}'>click here</a> to confirm your details.</p>"
                    "<p>Let us know if you have any concerns.</p>"
                    "<p>Best,<br>IT Support Team</p>"
                )
            }
        ]
    }

    response = requests.post(
        MAILJET_URL, json=data, auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY)
    )

    if response.status_code == 200:
        print(f"Email sent to {recipient_email}")
    else:
        print(f"Failed to send to {recipient_email}: {response.text}")
