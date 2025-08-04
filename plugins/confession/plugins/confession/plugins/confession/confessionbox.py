from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("confessionbox") & filters.group)
async def confession_box(client, message: Message):
    text = (
        "📥 *Anonymous Confession Box* 📥\n\n"
        "Send your secret messages anonymously! 🤫\n\n"
        "Just PM the bot and type:\n"
        "`/confess your message here`\n\n"
        "Your identity will be 100% hidden.\n\n"
        "🧑‍💼 Owner: @KRIYANSH_CHOUDHARY"
    )
    await message.reply(text)
