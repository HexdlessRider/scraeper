import asyncio
import os
import re
import time
import json

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from core.engine import fetch_url


async def scrape_data(file_name: str):
    url = 'https://ik-zoek.de-alliantie.nl/getproperties'
    payload_kopen = {
        'page': 1,
        'type': 'kopen',
        'sorting': 'rel',
        'order': 'desc'
    }
    payload_huren = {
        'page': 1,
        'type': 'huren',
        'sorting': 'rel',
        'order': 'desc'
    }
    payload_parkeren = {
        'page': 1,
        'type': 'parkeren',
        'sorting': 'rel',
        'order': 'desc'
    }
    payload_bedrijfsruimte = {
        'page': 1,
        'type': 'bedrijfsruimte',
        'sorting': 'rel',
        'order': 'desc'
    }
    result = []
    data_kopen = await fetch_url('POST', url, payload=payload_kopen)
    data_huren = await fetch_url('POST', url, payload=payload_huren)
    data_parkeren = await fetch_url('POST', url, payload=payload_parkeren)
    data_bedrijfsruimte = await fetch_url('POST', url, payload=payload_bedrijfsruimte)
    if data_kopen:
        result.extend(json.loads(data_kopen)['data'])
    if data_huren:
        result.extend(json.loads(data_huren)['data'])
    if data_parkeren:
        result.extend(json.loads(data_parkeren)['data'])
    if data_bedrijfsruimte:
        result.extend(json.loads(data_bedrijfsruimte)['data'])
    result = [{
        'url': 'https://ik-zoek.de-alliantie.nl/' + elm['url'],
        'rent_price': int(re.sub(r'\D', '', elm['price'])) if "kopen/" not in elm['url'] else None,
        'selling_price': int(re.sub(r'\D', '', elm['price'])) if "kopen/" in elm['url'] else None,
        'square_meters': elm['size'],
        'bedrooms': elm['rooms'],
        'location': f"{elm['url'].split('/')[-2].capitalize()}",
        'address': f"{elm['address']}"
    } for elm in result]

    if result:
        try:
            await ApartmentStore.create_or_update_apartment(result, file_name)
        except Exception as e:
            print(e)



async def main():
    script_path = os.path.abspath(__file__)
    script_name = (os.path.basename(script_path)).split('.')[0]
    while True:
        await scrape_data(file_name=script_name)
        await asyncio.sleep(VESTEDA_CD)



if __name__ == "__main__":
    asyncio.run(main())