from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

@Client.on_message(filters.command("viewconfession") & filters.user(OWNER_ID))
async def view_confession(client, message: Message):
    await message.reply(
        "📥 सभी गुप्त Confession सीधे आपके inbox में भेजे जा रहे हैं जब भी कोई भेजेगा।\n"
        "कोई स्टोर नहीं होता – सब कुछ live anonymous रहता है.\n\n"
        "_By: @KRIYANSH_CHOUDHARY_"
    )
