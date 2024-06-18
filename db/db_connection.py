import logging
from contextlib import asynccontextmanager

from supabase_py_async import create_client
from supabase_py_async.lib.client_options import ClientOptions
from settings.config import SUPABASE_URL, SUPABASE_KEY, SUPABASE_SECRET_KEY

client = None
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan():
    global client
    url: str = SUPABASE_URL
    key: str = SUPABASE_KEY
    secret_key: str = SUPABASE_SECRET_KEY
    if client is None:
        client = await create_client(url, key, secret_key,
                                     options=ClientOptions(
                                         postgrest_client_timeout=10, storage_client_timeout=10))
        try:
            logger.info("connect to db")
            yield client
        except Exception as e:
            logger.error(f"connect to db --- -- {str(e)}")
    else:
        yield client
