from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 5684410709))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6034357260 1511103739 1318247204").split()))
