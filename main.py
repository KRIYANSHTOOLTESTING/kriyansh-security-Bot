# 📁 main.py
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
import logging
import os

logging.basicConfig(level=logging.INFO)

# ✅ Load All Plugins
plugins = dict(root="plugins")

# ✅ Create Client
bot = Client(
    "roseplusplus_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
)

# ✅ Run Bot
if __name__ == "__main__":
    print("🤖 Bot Started as @KRIYANSH_CHOUDHARY")
    bot.run()
