from pyrogram import Client, filters
from pyrogram.types import Message
from database.mongodb import users, groups

@Client.on_message(filters.command("stats"))
async def stats(client, message: Message):
    total_users = await users.count_documents({})
    total_groups = await groups.count_documents({})

    await message.reply(
        f"📊 Bot Stats:\n\n👤 Users: `{total_users}`\n👥 Groups: `{total_groups}`\n\n_By: @KRIYANSH_CHOUDHARY_"
    )
