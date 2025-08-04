from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user's message to ban them.")

    user_id = message.reply_to_message.from_user.id
    try:
        await client.kick_chat_member(message.chat.id, user_id)
        await message.reply(f"🚫 Banned [user](tg://user?id={user_id})\n_By: @KRIYANSH_CHOUDHARY_")
    except:
        await message.reply("⚠️ Couldn't ban the user.")
