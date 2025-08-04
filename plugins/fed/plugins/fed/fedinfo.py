📁 plugins/fed/fedinfo.py

from pyrogram import Client, filters from pyrogram.types import Message from database.mongodb import feds, groups

@Client.on_message(filters.command("fedinfo") & filters.group) async def fed_info(client, message: Message): group = await groups.find_one({"id": message.chat.id}) if not group or "fed_id" not in group: return await message.reply("❌ Group not in any fed")

fed_id = group["fed_id"]
fed = await feds.find_one({"fed_id": fed_id})

await message.reply(
    f"📡 *Federation Info:*\n\n"
    f"🆔 Fed ID: `{fed_id}`\n"
    f"👑 Owner: `{fed['owner_id']}`\n"
    f"📛 Name: `{fed['fed_name']}`\n"
    f"🚫 FBans: `{len(fed['banned_users'])}`"
)

