from pyrogram import Client, filters
from pyrogram.types import Message
import time

@Client.on_message(filters.command("ping"))
async def ping_command(client, message: Message):
    start = time.time()
    reply = await message.reply("🏓 Pong!")
    end = time.time()
    ping_time = round((end - start) * 1000)
    await reply.edit_text(f"🏓 Pong: `{ping_time}ms`\n_By: @KRIYANSH_CHOUDHARY_")
