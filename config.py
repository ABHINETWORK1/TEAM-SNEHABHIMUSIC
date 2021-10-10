import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
OWNER_NAME = getenv("OWNER_NAME", "SNEHU_IS_MINE")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SNEHABHI_UPDATES")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/42317cd6618d736284b91.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SNEHU_MUSICS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SNEHABHI_SUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "SNEHABHI MUSICS")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/ABHINETWORK1/TEAM-SNEHABHIMUSIC")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
