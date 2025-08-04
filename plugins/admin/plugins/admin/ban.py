# 📁 plugins/admin/ban.py
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from pyrogram.enums import ChatMemberStatus

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("❌ सिर्फ admin ही इस command का इस्तेमाल कर सकते हैं।")

    if not message.reply_to_message:
        return await message.reply("⚠️ किसे ban करना है, उस पर reply करो।")

    user_id = message.reply_to_message.from_user.id

    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply(f"✅ {user_id} को ban कर दिया गया।\n_By: @KRIYANSH_CHOUDHARY_")
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

async def is_admin(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID
