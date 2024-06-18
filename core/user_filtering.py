import asyncio
import time

from db.models.apartment import ApartmentStore
from db.models.filter import FilterStore, FilterSchema
from db.models.user_apartment import UserApartmentStore
from settings.config import VESTEDA_CD


async def scan_filter():
    # Run all main functions concurrently
    filtered_apartments = {}
    user_filters = await FilterStore.get_filters()
    for filter in user_filters:
        clean_apart = await ApartmentStore.get_filtered_apartment(FilterSchema(**filter))
        filtered_apartments[filter['user_id']] = clean_apart
        if filtered_apartments:
            await UserApartmentStore.create_task(filter['user_id'], filtered_apartments)


async def main():
    while True:
        await scan_filter()
        await asyncio.sleep(VESTEDA_CD * 2)


if __name__ == "__main__":
    asyncio.run(main())
