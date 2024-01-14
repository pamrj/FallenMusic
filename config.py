from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1000"))

OWNER_ID = int(getenv("OWNER_ID"6613385650))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2c117fb863ee800f83c27.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2c117fb863ee800f83c27.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/allexamquiznew")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Stylish_Bio_Telegram_xyz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
