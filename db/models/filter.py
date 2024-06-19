import asyncio
import json
import logging

from aioredis import Redis
from pydantic import BaseModel, ValidationError

from db.db_connection import lifespan

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from settings.config import REDIS_HOST, REDIS_PORT

rb = Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)


class FilterSchema(BaseModel):
    user_id: str
    min_price: float | None = None
    max_price: float | None = None
    min_square_meters: int | None = None
    furnished: bool | None = None
    location: str | None = None
    # is_student: bool | None = None
    # exclude_senior_housing: bool | None = None


class FilterStore:
    @staticmethod
    async def get_filters():
        async with lifespan() as client:
            tasks = await client.table("filters").select("*").execute()
            # await rb.set("user_filters", json.dumps(tasks.data))
            return tasks.data
