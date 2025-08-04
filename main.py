# 📁 main.py

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
import sys
import os

# ✔️ Logging setup (Debug purpose)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

# ✔️ Ensure plugins folder exists
if not os.path.isdir("plugins"):
    logger.error("❌ 'plugins' folder missing. Make sure you have all plugin modules!")
    sys.exit(1)

# ✔️ Create Pyrogram Client with Bot Token
app = Client(
    "bawal_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")  # Load all plugin folders
)

# ✔️ Start the bot
if __name__ == "__main__":
    print("🤖 Bot is starting... Powered by @KRIYANSH_CHOUDHARY")
    try:
        app.run()
    except Exception as e:
        logger.error(f"🔥 Bot Crashed: {e}")
