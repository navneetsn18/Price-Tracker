import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from dotenv import load_dotenv

load_dotenv()

def sendEmail(username, to, product, url, currentPrice):

    # Set up the SMTP server connection
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_username = os.getenv("MAILING_USERNAME")
    smtp_password = os.getenv("MAILING_PASSWORD")
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)

    html = """
    <!DOCTYPE html>
    <html>

    <head>
    <meta charset="UTF-8">
    <title>Product Price Update</title>
    <!-- Import Material UI stylesheets -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" />

    <style>
        /* Set global styles */
        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        }

        body {
        background: linear-gradient(to bottom, #f0f2f5, #f5f6f8);
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: Arial, sans-serif;
        font-size: 14px;
        line-height: 1.5;
        margin: 0;
        padding: 0;
        }


        /* Set Material UI styles */
        .container {
        margin: 100px auto;
        max-width: 600px;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        }

        h1 {
        font-size: 24px;
        margin: 0 0 20px;
        font-weight: 500;
        }

        p {
        margin-bottom: 16px;
        color: #444;
        font-size: 16px;
        line-height: 1.5;
        }

        strong {
        font-weight: 500;
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

        a {
        color: #007bff;
        text-decoration: none;
        font-weight: 500;
        }

        a:hover {
        text-decoration: underline;
        }

        i {
        margin-right: 5px;
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
        <li>
            <span class="label">Product URL:</span>
            <a href="{{product_url}}" class="value">
            <i class="fas fa-external-link-alt"></i>
            {{product_url}}
            </a>
        </li>
        </ul>
    </div>

    <!-- Import Material UI scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js"></script>
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
