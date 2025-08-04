from pyrogram import Client, filters
from pyrogram.types import Message
import time
from config import START_TIME

def get_readable_time(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return f"{d}d {h}h {m}m {s}s"

@Client.on_message(filters.command("uptime"))
async def show_uptime(client, message: Message):
    uptime_sec = int(time.time() - START_TIME)
    uptime = get_readable_time(uptime_sec)
    await message.reply(f"⏱ Uptime: `{uptime}`\n_By: @KRIYANSH_CHOUDHARY_")
