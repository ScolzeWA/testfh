from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "13382519"))
API_HASH = getenv("API_HASH", "3c852e55d6ef31f7acd8e4a666465e07")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𝑾𝑶𝑹𝑳𝑫 𝑴𝑼𝑺𝑰𝑪 💗ˣ")
BOT_USERNAME = getenv("BOT_USERNAME", "WorldMusicly_Bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Gr_World_Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1491415522 1419419100 2112059230").split()))
