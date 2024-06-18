import asyncio
import os
import time
import json

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from core.engine import fetch_url
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def scrape_data(file_name: str):
    logger.info(f"Scraping data from {file_name}")
    url = 'https://www.vesteda.com/api/units/search/facet'
    payload = {
        "filters": [0],
        "latitude": 0,
        "longitude": 0,
        "place": "",
        "placeObject": {"placeType": "0", "name": "", "latitude": "0", "longitude": "0"},
        "placeType": 0,
        "radius": 20,
        "sorting": 0,
        "priceFrom": 500,
        "priceTo": 9999,
        "language": "en"
    }
    data = await fetch_url('POST', url, 1, payload=payload)
    result = [{
        'url': 'https://www.vesteda.com' + elm['url'],
        'rent_price': int(elm['priceUnformatted']),
        'square_meters': elm['size'],
        'bedrooms': elm['numberOfBedRooms'],
        'location': elm['location'],
        # clear_info # ???
    } for elm in json.loads(data)['results']['objects']]

    if result:
        await ApartmentStore.create_or_update_apartment(result, file_name)
        # await check uniq result (service class in db)
        # await store uniq result (service class in db )
        # wait next function call
        # print(result
        #       )
    return result


async def main():
    while True:
        script_path = os.path.abspath(__file__)
        script_name = (os.path.basename(script_path)).split('.')[0]
        await scrape_data(file_name=script_name)

        # asyncio.run(scrape_data(file_name=script_name))
        time.sleep(VESTEDA_CD)


if __name__ == "__main__":
    asyncio.run(main())
