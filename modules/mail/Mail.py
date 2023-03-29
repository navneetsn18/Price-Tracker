import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the SMTP server connection
smtp_server = "smtp-relay.sendinblue.com"
smtp_port = os.getenv("SMTP_PORT")
smtp_username = os.getenv("MAILING_USERNAME")
smtp_password = os.getenv("MAILING_PASSWORD")
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()
smtp_connection.login(smtp_username, smtp_password)

# Create the message object


def sendEmail(username, to, product, url, currentPrice):
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Product Price Update</title>
        <style>
            body {
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                font-size: 14px;
                line-height: 1.5;
                margin: 0;
                padding: 0;
            }
            .container {
                margin: 20px auto;
                max-width: 600px;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h1 {
                font-size: 24px;
                margin: 0 0 20px;
            }
            ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            li {
                margin-bottom: 10px;
            }
            .label {
                display: inline-block;
                min-width: 100px;
                font-weight: bold;
                margin-right: 10px;
            }
            .value {
                display: inline-block;
                word-break: break-all;
            }
            .price {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Product Price Update</h1>
            <p>Dear <strong>{{username}}</strong>,</p>
            <p>The price of your product <strong>{{product_name}}</strong> has been updated. The current price is <span class="price">{{product_price}}</span>.</p>
            <p>You can access the product by following this link:</p>
            <ul>
                <li><span class="label">Product URL:</span> <a href="{{product_url}}" class="value">{{product_url}}</a></li>
            </ul>
        </div>
    </body>
    </html>
    """
    html = html.replace('{{username}}', username)
    html = html.replace('{{product_name}}', product)
    html = html.replace('{{product_price}}', str(currentPrice))
    html = html.replace('{{product_url}}', url)

    from_email = "testingfornsn@gmail.com"
    to_email = to
    subject = "ALERT!! Price DROP"
    body = "This is a test email sent from Python."
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    # Send the email
    smtp_connection.sendmail(from_email, to_email, message.as_string())

    # Close the SMTP server connection
    smtp_connection.quit()
