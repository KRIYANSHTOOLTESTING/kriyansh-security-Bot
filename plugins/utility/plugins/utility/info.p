from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("info"))
async def user_info(client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("❌ Please reply to a user to get info.")

    user = reply.from_user
    text = (
        f"👤 User Info:\n\n"
        f"ID: `{user.id}`\n"
        f"First Name: `{user.first_name}`\n"
        f"Username: @{user.username if user.username else 'None'}\n"
        f"Is Bot: `{user.is_bot}`\n"
        f"Language Code: `{user.language_code if user.language_code else 'N/A'}`\n\n"
        f"_By: @KRIYANSH_CHOUDHARY_"
    )
    await message.reply(text)
