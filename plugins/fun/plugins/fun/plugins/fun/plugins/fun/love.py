from pyrogram import Client, filters
from pyrogram.types import Message
import random

loves = [
    "तुम्हारी हँसी तो दिल चुरा ले जाती है ❤️",
    "तेरी आँखों में कुछ खास बात है, जैसे पूरा आसमान समाया हो 💫",
    "तू मिल जाए तो पूरी दुनिया भूल जाऊं 💘",
    "मोहब्बत भी तुमसे और शिकायत भी तुमसे 😍",
    "तेरे बिना दिल अधूरा सा लगता है 💔"
]

@Client.on_message(filters.command("love"))
async def send_love(client, message: Message):
    l = random.choice(loves)
    await message.reply(f"❤️ Love Line:\n\n{l}\n\n_By: @KRIYANSH_CHOUDHARY_")
