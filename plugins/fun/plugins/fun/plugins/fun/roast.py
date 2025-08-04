from pyrogram import Client, filters
from pyrogram.types import Message
import random

roasts = [
    "तेरे जैसे लोग तो WiFi के signal जैसे होते हैं — आते-जाते रहते हैं 😏",
    "तेरी शक्ल देख कर तो captcha भी confuse हो जाए 😂",
    "तू पैदा नहीं हुआ था, format हो गया था 🧠",
    "तेरे jokes इतने dry हैं कि मरुस्थल में बारिश हो जाए 🌵",
    "तेरी vibe Windows XP जैसी है — पुरानी और slow 🐢"
]

@Client.on_message(filters.command("roast"))
async def send_roast(client, message: Message):
    r = random.choice(roasts)
    await message.reply(f"🔥 Roast:\n\n{r}\n\n_By: @KRIYANSH_CHOUDHARY_")
