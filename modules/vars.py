from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = "26115463"
API_HASH = "054557eca362bba15769130a5fadf0de"
BOT_TOKEN = "6937159126:AAH72DSnASIuf4eMWJbwc63HcvXev5qMbF0"
OWNER_ID = "6631088681"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6631088681").split()))
