from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("adminlist") & filters.group)
async def list_admins(client, message: Message):
    admins = await client.get_chat_members(message.chat.id, filter="administrators")

    admin_text = "👮 Admins in this group:\n"
    for admin in admins:
        user = admin.user
        admin_text += f"- {user.mention} | `{user.id}`\n"

    await message.reply(admin_text + "\n_By: @KRIYANSH_CHOUDHARY_")
