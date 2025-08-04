from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.mongodb import groups

@Client.on_message(filters.command("globallock") & filters.user(OWNER_ID))
async def lock_group(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /globallock group_id")

    group_id = int(message.command[1])
    groups.update_one({"id": group_id}, {"$set": {"locked": True}}, upsert=True)
    await message.reply(f"🔒 Group `{group_id}` has been locked.\n_By: @KRIYANSH_CHOUDHARY_")

@Client.on_message(filters.command("globalunlock") & filters.user(OWNER_ID))
async def unlock_group(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /globalunlock group_id")

    group_id = int(message.command[1])
    groups.update_one({"id": group_id}, {"$set": {"locked": False}}, upsert=True)
    await message.reply(f"🔓 Group `{group_id}` has been unlocked.\n_By: @KRIYANSH_CHOUDHARY_")
