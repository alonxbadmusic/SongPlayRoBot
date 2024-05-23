import os
API_ID = int(os.getenv("20401009"))
API_HASH = os.getenv("6445b43e4af228532e84848d1bb2eb64")
BOT_TOKEN = os.getenv("6724904318:AAGEvKV3zXiyad9jU_e7rogQCjFMmAXaimg")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
