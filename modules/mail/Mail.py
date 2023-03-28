import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the SMTP server connection
smtp_server = "smtp-relay.sendinblue.com"
smtp_port = 587
smtp_username = os.getenv("MAILING_USERNAME")
smtp_password = os.getenv("MAILING_PASSWORD")
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Create the message object
def sendEmail(to,product,link,):
    from_email = "testingfornsn@gmail.com"
    to_email = to
    subject = "ALERT!! Price DROP"
    body = "This is a test email sent from Python."
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email
    smtp_connection.sendmail(from_email, to_email, message.as_string())

# Close the SMTP server connection
smtp_connection.quit()
