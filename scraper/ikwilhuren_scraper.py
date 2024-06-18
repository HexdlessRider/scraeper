import asyncio
import logging
import os
import re
import time
import json

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from bs4 import BeautifulSoup
from core.engine import fetch_url


async def scrape_data(file_name: str):
    url = "https://ikwilhuren.nu/aanbod/"

    r = await fetch_url('GET', url)

    count_item_str = BeautifulSoup(r, "html.parser").find("span", class_="ff-roboto-slab").text
    count_item = int(re.sub(r"[^\d,]", "", count_item_str))
    print(count_item)
    result = []
    for page in range(1, (count_item // 10) + 1):
        page_url = f'https://ikwilhuren.nu/aanbod/?page={page}'
        res = await fetch_url('GET', page_url)
        if not res:
            logging.error(f"Failed to fetch data from {page_url}")
            continue  # Skip this iteration if no response is received
        try:
            res_soup = BeautifulSoup(res, "html.parser")
            cards = res_soup.find_all(class_='card-woning')
            for card in cards:
                url = card.find(class_='stretched-link').get('href')
                if 'http' not in url:
                    url = 'https://ikwilhuren.nu' + url
                data = card.find(class_='dotted-spans').text.split('\n')
                _, price, d = card.find(class_='dotted-spans').text.split('\n')
                try:
                    sq_feet, bedrooms = d.split(' m2 ')
                except:
                    sq_feet = ''
                    bedrooms = d
                address = ' '.join(card.find(class_='stretched-link').text.strip().split(' ')[1:])
                city = card.find(class_='card-body').text.split('\n')[6].split(' ')[1]

                price = int(re.sub(r"[^\d^]", "", price))
                if sq_feet:
                    sq_feet = int(re.sub(r"[^\d^]", "", str(sq_feet)))
                if bedrooms:
                    bedrooms = int(re.sub(r"[^\d^]", "", bedrooms))
                result.append({
                    'url': url,
                    'rent_price': price,
                    'square_meters': None if sq_feet == "" else int(sq_feet),
                    'bedrooms': None if bedrooms == "" else int(bedrooms),
                    'location': f"{city}, {address}",
                })
        except Exception as e:
            logging.error(f"Error processing page {page_url}: {e}")


async def main():
    script_path = os.path.abspath(__file__)
    script_name = (os.path.basename(script_path)).split('.')[0]
    while True:
        await scrape_data(file_name=script_name)
        time.sleep(VESTEDA_CD)


if __name__ == "__main__":
    asyncio.run(main())
