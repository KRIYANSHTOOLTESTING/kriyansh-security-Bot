from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("alive"))
async def alive_status(client, message: Message):
    await message.reply(
        "✅ *Bot is Alive & Running!*\n\n"
        "👑 Owner: @KRIYANSH_CHOUDHARY\n"
        "💻 Powered by: Pyrogram\n"
        "🚀 Version: Rose++ Custom Bot\n\n"
        "Use /help to see available commands."
    )
