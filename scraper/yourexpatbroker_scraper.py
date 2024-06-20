import asyncio
import os
import time
import json
from bs4 import BeautifulSoup
import re

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from core.engine import fetch_url


async def scrape_data(file_name: str):
    num = 0
    result = []
    while True:
        url = f"https://yourexpatbroker.nl/en-gb/residential-listings/rent?skip={num}"
        data = await fetch_url('GET', url, 1)
        if not data:
            break
        results = BeautifulSoup(data, "html.parser").find_all("div", class_="object")

        if len(results) <= 0:
            break

        for res in results:
            if 'rented' in str(res.find(class_="object_status")):
                continue
            address = str(res.find("span", class_="street").contents[0])
            city = str(res.find("span", class_="locality").contents[0])
            url = "https://yourexpatbroker.nl" + res.find("a", class_="saletitle")["href"].split('?')[0]

            numeric_value = re.sub(r"[^\d,]", "", str(res.find("span", class_="obj_price").contents[0]))
            price = int(numeric_value.replace(",", ""))
            sq_feet_str = str(res.find("span", class_="object_sqfeet").text)
            sq_feet = int(re.sub(r"[^\d,]", "", sq_feet_str))

            bedrooms_str = res.find("span", class_="object_bed_rooms").text
            bedrooms = int(re.sub(r"[^\d,]", "", bedrooms_str))

            try:
                furnished_str = res.find("span", class_="object_fitment_furnished")
                if furnished_str.text.strip() == 'Furnished':
                    furnished = True
                else:
                    furnished = False
            except:
                furnished = False

            result.append({
                'url': url,
                'rent_price': price,
                'square_meters': sq_feet,
                'bedrooms': bedrooms,
                'location': f"{city}",
                'address': f"{address}",
                'furnished': furnished
            })
        num += 10

    if result:
        await ApartmentStore.create_or_update_apartment(result, file_name)
        # await check uniq result (service class in db)
        # await store uniq result (service class in db )
        # wait next function call
        pass


async def main():
    script_path = os.path.abspath(__file__)
    script_name = (os.path.basename(script_path)).split('.')[0]
    while True:
        await scrape_data(file_name=script_name)
        await asyncio.sleep(VESTEDA_CD)


if __name__ == "__main__":
    asyncio.run(main())
