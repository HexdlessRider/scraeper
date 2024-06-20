import asyncio
import logging
import smtplib
from email.mime.text import MIMEText
from settings.config import GMAIL_EMAIL, GMAIL_PASSWORD, MAIL_HOST, MAIL_PORT
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_email(subject, body, recipients, sender=GMAIL_EMAIL, password=GMAIL_PASSWORD):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    # Create an executor for asynchronous operation
    loop = asyncio.get_event_loop()

    try:
        smtp_server = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
        smtp_server.starttls()

        # Login using the executor
        await loop.run_in_executor(None, smtp_server.login, sender, password)

        # Send email using the executor
        await loop.run_in_executor(None, smtp_server.send_message, msg)
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        logger.error(e)
        return False

    finally:
        # Ensure the connection is closed
        smtp_server.quit()
