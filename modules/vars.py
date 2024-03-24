from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = "gdjdhdbdndb"
API_HASH = "65c4b51f54049ebe22bc01fd9a95575b"
BOT_TOKEN = "6806206800:AAHpkIk7pL3RyvJ4EOPS5Vbk2m79u03S6Ss"
OWNER_ID = "6401497985"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6401497985").split()))
