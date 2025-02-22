import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load email list from Excel
df = pd.read_excel("emails.xlsx")  # Ensure this file exists

# Your Gmail credentials
sender_email = "your_email@gmail.com"
app_password = "your_generated_app_password"  # Use App Password, not your real password

canary_link = "https://your-canary-token-link"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

# Loop through recipients
for index, row in df.iterrows():
    receiver_email = row["Email"]
    name = row["Name"]

    # Email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Important Security Update"
    
    body = f"Hello {name},\n\nPlease check this important security update: {canary_link}\n\nBest,\nCybersecurity Team"
    msg.attach(MIMEText(body, "plain"))

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())

server.quit()
print("Emails sent successfully!")
