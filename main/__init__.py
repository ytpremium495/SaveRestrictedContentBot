#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "27824890"default=None, cast=int)
API_HASH = config("API_HASH", "e9a93f2f9e421ba2e11901d189376eef"default=None)
BOT_TOKEN = config("BOT_TOKEN", "5940975704:AAHvQnmcGRCLoqxSB8DNedWJVBwHV4jsKqA"default=None)
SESSION = config("SESSION", "BQGokvoAtpOM8Gthq8Cs_djYMY0WM9XB0xTTO98WsO6_hNQaQOgVcUkY_i-M7gqB87ssv3xRIJ7l3gcUaTs3ML4eSeypx6eivxmHZ4uye-q3zA21A4f23MO5vUqHpA5uCLjpNwj3WpDYgSUsEO46-yCp7-h-0qRbMzKpcxECq1tEFFOaYI4Wc9RCNrfQrsTwsrHVr7JWB05QEsAWrzxb76J5ywotLUmu2cXaV_R50jhwCzSpwQxbDvJ89cogfX3kqVoS0hIObs49EkGD0TEjtFvTJBDIZihcwdb8uJhkU_oDmSYkbCadAPmGbI-u4mxl0MBs9ixfjFWDPY5B2M2ldYYlR5PizQAAAAF1HkH7AA"default=None)
FORCESUB = config("FORCESUB", "bollywood_hollywoodmovies0"default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
