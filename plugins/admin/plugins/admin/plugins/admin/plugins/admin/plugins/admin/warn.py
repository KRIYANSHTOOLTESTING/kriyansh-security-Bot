# 📁 plugins/admin/warn.py
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from pyrogram.enums import ChatMemberStatus

warns = {}

@Client.on_message(filters.command("warn") & filters.group)
async def warn_user(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("❌ सिर्फ admin ही warn कर सकता है।")

    if not message.reply_to_message:
        return await message.reply("⚠️ किसी को reply करो जिसे warn देना है।")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    warns.setdefault(chat_id, {})
    warns[chat_id].setdefault(user_id, 0)

    warns[chat_id][user_id] += 1
    count = warns[chat_id][user_id]

    if count >= 3:
        try:
            await client.ban_chat_member(chat_id, user_id)
            warns[chat_id][user_id] = 0
            await message.reply(f"🚫 3 warns के बाद {user_id} ban कर दिया गया।\n_By: @KRIYANSH_CHOUDHARY_")
        except Exception as e:
            await message.reply(f"❌ Ban Error: {e}")
    else:
        await message.reply(f"⚠️ Warn दिया गया [ {count}/3 ]\n_By: @KRIYANSH_CHOUDHARY_")

async def is_admin(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID
