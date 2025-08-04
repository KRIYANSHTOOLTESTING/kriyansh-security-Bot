from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.mongodb import groups

@Client.on_message(filters.command("income") & filters.user(OWNER_ID))
async def show_income(client, message: Message):
    total_groups = await groups.count_documents({})
    locked_groups = await groups.count_documents({"locked": True})
    approved = total_groups - locked_groups

    income = approved * 50  # ₹50 per group
    await message.reply(
        f"💰 *@KRIYANSH_CHOUDHARY Stats:*\n\n"
        f"👥 Total Groups: `{total_groups}`\n"
        f"🔒 Locked: `{locked_groups}`\n"
        f"✅ Approved: `{approved}`\n"
        f"💵 Income Estimate: ₹{income}"
    )
