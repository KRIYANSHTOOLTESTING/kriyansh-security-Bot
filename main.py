# main.py

from pyrogram import Client
import logging
from config import API_ID, API_HASH, BOT_TOKEN

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# BOT Client (Bot Token based, NO session)
app = Client(
    name="bot",  # no session file will be saved
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}
)

if __name__ == "__main__":
    print("🤖 Bot is starting... Powered by @KRIYANSH_CHOUDHARY")
    try:
        app.run()
    except Exception as e:
        logger.error(f"🔥 Bot Crashed: {e}")
