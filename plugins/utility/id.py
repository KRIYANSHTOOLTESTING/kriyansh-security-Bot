from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("id"))
async def get_id(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    text = f"🆔 Info:\nUser ID: `{user_id}`\nChat ID: `{chat_id}`\n"

    if message.reply_to_message:
        text += f"\n👤 Replied User ID: `{message.reply_to_message.from_user.id}`"

    await message.reply(text + "\n_By: @KRIYANSH_CHOUDHARY_")
