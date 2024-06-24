import os
from dotenv import load_dotenv
load_dotenv()
# arg = os.getenv("arg")

GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')
GMAIL_EMAIL = os.environ.get('GMAIL_EMAIL')
MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587

META_BASE_URL = os.environ.get('META_BASE_URL', "")
META_ACCESS_TOKEN = os.environ.get('META_ACCESS_TOKEN', "")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
SUPABASE_SECRET_KEY = os.environ.get("SUPABASE_SECRET_KEY")


REDIS_HOST = os.environ.get('REDIS_HOST', "redis")
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = os.environ.get('REDIS_DB', 0)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

VESTEDA_CD = int(os.environ.get('VESTEDA_CD', 1800))
