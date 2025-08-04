from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

@Client.on_message(filters.command("confess") & filters.private)
async def send_confession(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /confess Your message")

    confession_text = message.text.split(None, 1)[1]

    try:
        await client.send_message(
            OWNER_ID,
            f"📨 *New Confession:*\n\n`{confession_text}`\n\n(From an anonymous user)\n_By: @KRIYANSH_CHOUDHARY_"
        )
        await message.reply("✅ Your confession has been sent anonymously!")
    except Exception:
        await message.reply("⚠️ Failed to send confession.")
