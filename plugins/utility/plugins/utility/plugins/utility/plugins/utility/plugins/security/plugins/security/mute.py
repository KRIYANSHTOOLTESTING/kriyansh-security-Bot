from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Reply to a user's message to mute them.")

    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            permissions=ChatPermissions()
        )
        await message.reply(f"🔇 Muted [user](tg://user?id={user_id})\n_By: @KRIYANSH_CHOUDHARY_")
    except:
        await message.reply("⚠️ Couldn't mute the user.")
