import asyncio
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

from settings.config import GMAIL_EMAIL, GMAIL_PASSWORD, MAIL_HOST, MAIL_PORT

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_email(subject, body, recipients, sender=GMAIL_EMAIL, password=GMAIL_PASSWORD):
    email_body = MIMEText(body, "html")

    # Create a MIMEMultipart object and attach the email body
    email_message = MIMEMultipart()
    email_message["From"] = "Instarent"
    email_message["To"] = recipients
    email_message["Subject"] = subject
    email_message.attach(email_body)

    # Create an executor for asynchronous operation
    loop = asyncio.get_event_loop()

    try:
        smtp_server = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
        smtp_server.starttls()

        # Login using the executor
        await loop.run_in_executor(None, smtp_server.login, sender, password)

        # Send email using the executor
        await loop.run_in_executor(None, smtp_server.send_message, email_message)
        logger.info('Email sent')
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        logger.error(e)
        return False

    finally:
        # Ensure the connection is closed
        smtp_server.quit()


async def send_email_with_credentials(body, recipients, name):

    try:
        subject = "New apartments"
        env = Environment(loader=FileSystemLoader('templates/'))
        template = env.get_template("email.html")
        body = template.render(name=name, apartments=body)
        await send_email(subject, body, recipients)
        return True
    except Exception as e:
        logger.error(f"Failed to send email credentials: {e}")
        return False

# asyncio.run(send_email_with_credentials([{
#     "name": "name",
#     "price": "price",
#     "location": "location",
#     "address": "address",
#     "bedrooms": "bedrooms",
#     "square_meters": "square_meters"
# }, {
#     "name": "name1",
#     "price": "price1",
#     "location": "location1",
#     "address": "address1",
#     "bedrooms": "bedrooms1",
#     "square_meters": "square_meters1"
# }], "tonek84243@dcbin.com"))


