from pyrogram import Client, filters
from pyrogram.types import Message
import random

quotes = [
    "कोशिश करने वालों की कभी हार नहीं होती।",
    "खुद को कमजोर समझना सबसे बड़ा अपराध है।",
    "सपने वो नहीं जो नींद में आए, सपने वो हैं जो नींद ही ना आने दें।",
    "जो खुद की मदद करता है, भगवान भी उसी की मदद करता है।",
    "डर के आगे जीत है।"
]

@Client.on_message(filters.command("quote"))
async def random_quote(client, message: Message):
    q = random.choice(quotes)
    await message.reply(f"📜 Motivational Quote:\n\n{q}\n\n_By: @KRIYANSH_CHOUDHARY_")
