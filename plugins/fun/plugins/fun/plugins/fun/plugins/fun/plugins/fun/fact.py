from pyrogram import Client, filters
from pyrogram.types import Message
import random

facts = [
    "हाथी पानी में तैर सकते हैं और मीलों तक बिना थके तैरते रहते हैं 🐘",
    "मनुष्य का दिमाग एक दिन में 70,000 विचार बना सकता है 🧠",
    "शहद कभी खराब नहीं होता — हजारों साल तक भी नहीं! 🍯",
    "आपका दिल एक दिन में लगभग 1 लाख बार धड़कता है ❤️",
    "Octopus के तीन दिल होते हैं और नीला खून होता है 🐙"
]

@Client.on_message(filters.command("fact"))
async def send_fact(client, message: Message):
    f = random.choice(facts)
    await message.reply(f"📚 Fun Fact:\n\n{f}\n\n_By: @KRIYANSH_CHOUDHARY_")
