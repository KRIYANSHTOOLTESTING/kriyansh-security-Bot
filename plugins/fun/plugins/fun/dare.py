from pyrogram import Client, filters
from pyrogram.types import Message
import random

dares = [
    "अपने crush को अभी message करो - 'I Like You' 😳",
    "Group में सबसे बोर इंसान को publicly compliment दो 😆",
    "5 बार 'Main Pagal Hoon' बोलो और वीडियो भेजो 😂",
    "अपने status पर 1 घंटे के लिए 'I am noob' लगाओ 🤡",
    "पिछले 5 chat screenshots group में भेजो 📱",
    "किसी को call करो और 'I love you' बोल दो 📞"
]

@Client.on_message(filters.command("dare"))
async def send_dare(client, message: Message):
    d = random.choice(dares)
    await message.reply(f"🔥 Dare:\n\n{d}\n\n_By: @KRIYANSH_CHOUDHARY_")
