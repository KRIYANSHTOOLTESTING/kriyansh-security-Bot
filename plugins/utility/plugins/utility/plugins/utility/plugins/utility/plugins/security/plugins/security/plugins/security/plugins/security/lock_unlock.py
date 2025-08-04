from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

@Client.on_message(filters.command("lock") & filters.group)
async def lock_group(client, message: Message):
    await client.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions()
    )
    await message.reply("🔒 Group locked! Only admins can chat now.\n_By: @KRIYANSH_CHOUDHARY_")

@Client.on_message(filters.command("unlock") & filters.group)
async def unlock_group(client, message: Message):
    await client.set_chat_permissions(
        chat_id=message.chat.id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_stickers=True,
            can_send_animations=True,
            can_send_games=True,
            can_use_inline_bots=True,
            can_add_web_page_previews=True,
            can_send_polls=True,
            can_invite_users=True,
        )
    )
    await message.reply("🔓 Group unlocked! Everyone can chat now.\n_By: @KRIYANSH_CHOUDHARY_")
