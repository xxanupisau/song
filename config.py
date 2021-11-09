import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴜғᴏ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/SIRIA-11-09")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/SIRIA-11-09")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/SIRIA-11-09")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/SIRIA-11-09")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "C94_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "U_U_U_Q")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xv00v")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xv00v")
OWNER_NAME = getenv("OWNER_NAME", "U_U_U_Q") 
DEV_NAME = getenv("DEV_NAME", "U_U_U_Q")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
