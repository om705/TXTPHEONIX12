from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = "22114233"
API_HASH = "d7abcec5c967414fadb1d438fa05ebea"
BOT_TOKEN = "6732431727:AAENFa5Btpk_EPF5nY0DUUpm6i6WPCIC2hM"
OWNER_ID = "1403488629"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1403488629").split()))
