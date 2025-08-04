📁 plugins/fed/createfed.py

from pyrogram import Client, filters from pyrogram.types import Message from config import OWNER_ID from database.mongodb import feds

@Client.on_message(filters.command("createfed") & filters.user(OWNER_ID)) async def create_fed(client, message: Message): if len(message.command) < 2: return await message.reply("❌ Usage: /createfed FedName")

fed_name = message.command[1]
fed_id = f"fed_{message.from_user.id}_{fed_name.lower()}"

existing = await feds.find_one({"fed_id": fed_id})
if existing:
    return await message.reply("⚠️ Fed already exists!")

await feds.insert_one({
    "fed_id": fed_id,
    "owner_id": message.from_user.id,
    "fed_name": fed_name,
    "banned_users": []
})
await message.reply(f"✅ Fed `{fed_name}` created successfully!")

📁 plugins/fed/joinfed.py

from pyrogram import Client, filters from pyrogram.types import Message from config import OWNER_ID from database.mongodb import feds, groups

@Client.on_message(filters.command("joinfed") & filters.group) async def join_fed(client, message: Message): if len(message.command) < 2: return await message.reply("❌ Usage: /joinfed fed_id")

fed_id = message.command[1]
fed = await feds.find_one({"fed_id": fed_id})
if not fed:
    return await message.reply("⚠️ No such federation found.")

await groups.update_one({"id": message.chat.id}, {"$set": {"fed_id": fed_id}}, upsert=True)
await message.reply(f"✅ Group joined federation: `{fed['fed_name']}`")

📁 plugins/fed/fban.py

from pyrogram import Client, filters from pyrogram.types import Message from config import OWNER_ID from database.mongodb import feds, groups

@Client.on_message(filters.command("fban") & filters.group) async def fban_user(client, message: Message): if not message.reply_to_message: return await message.reply("⚠️ Reply to a user to fban")

user_id = message.reply_to_message.from_user.id
group = await groups.find_one({"id": message.chat.id})
if not group or "fed_id" not in group:
    return await message.reply("⚠️ This group is not part of any federation")

fed_id = group["fed_id"]
await feds.update_one({"fed_id": fed_id}, {"$addToSet": {"banned_users": user_id}})

await message.reply(f"🚫 User `{user_id}` FBanned in fed `{fed_id}`")

# Optionally, auto-kick
try:
    await client.ban_chat_member(message.chat.id, user_id)
except:
    pass

📁 plugins/fed/funfedinfo.py

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

