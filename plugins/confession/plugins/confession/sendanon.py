from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID

@Client.on_message(filters.command("sendanon") & filters.user(OWNER_ID))
async def send_anonymous(client, message: Message):
    if len(message.command) < 3:
        return await message.reply("❌ Usage: /sendanon user_id message")

    user_id = int(message.command[1])
    anon_msg = message.text.split(None, 2)[2]

    try:
        await client.send_message(
            user_id,
            f"💌 Anonymous Message:\n\n{anon_msg}\n\n_By: @KRIYANSH_CHOUDHARY_"
        )
        await message.reply("✅ Message sent anonymously!")
    except:
        await message.reply("⚠️ Failed to send anonymous message.")
