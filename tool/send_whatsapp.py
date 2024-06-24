import asyncio
import logging

import httpx
import requests

from settings import config
from tool.utils import generate_rental_listings_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_whatsapp(message: str, phone_number: str):
    headers = {
        'Authorization': f'Bearer {config.META_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }


    data = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(config.META_BASE_URL, headers=headers, json=data)
        if response.status_code == 200:
            print(response.json())
            logging.info("Message sent successfully!")
            print(f"Response content: {response.text}")

        else:
            logging.info("Failed to send message:", response.text)


