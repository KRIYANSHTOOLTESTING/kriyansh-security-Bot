from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("unban") & filters.group)
async def unban_user(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /unban user_id")

    try:
        user_id = int(message.command[1])
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply(f"✅ Unbanned user `{user_id}`\n_By: @KRIYANSH_CHOUDHARY_")
    except:
        await message.reply("⚠️ Couldn't unban the user.")
