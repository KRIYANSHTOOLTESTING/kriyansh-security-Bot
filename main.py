# main.py

from pyrogram import Client
import logging
from config import API_ID, API_HASH, BOT_TOKEN

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pyrogram Bot Client (Bot Token Based - No OTP, No session)
app = Client(
    name=":memory:",  # Prevents session creation
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"}  # Load all plugin folders
)

# Start the bot
if __name__ == "__main__":
    print("🤖 Bot is starting... Powered by @KRIYANSH_CHOUDHARY")
    try:
        app.run()
    except Exception as e:
        logger.error(f"🔥 Bot Crashed: {e}")
