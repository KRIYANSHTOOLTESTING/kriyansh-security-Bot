from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.mongodb import users

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_msg(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /broadcast Your message here")

    text = message.text.split(None, 1)[1]
    success, failed = 0, 0

    async for user in users.find():
        try:
            await client.send_message(user['id'], f"📢 Broadcast:\n\n{text}\n\n_By: @KRIYANSH_CHOUDHARY_")
            success += 1
        except:
            failed += 1

    await message.reply(f"✅ Broadcast completed!\nSuccess: {success} | Failed: {failed}")
