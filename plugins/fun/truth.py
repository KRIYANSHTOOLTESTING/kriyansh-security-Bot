from pyrogram import Client, filters
from pyrogram.types import Message
import random

truths = [
    "क्या तुमने कभी किसी को cheat किया है?",
    "तुम्हारा सबसे शर्मनाक पल कौन सा था?",
    "क्या तुम आज भी अपने ex को याद करते हो?",
    "तुम्हारा सबसे गंदा राज़ क्या है?",
    "तुम किससे सबसे ज़्यादा जलते हो?",
    "तुम्हारा crush कौन है अभी?"
]

@Client.on_message(filters.command("truth"))
async def send_truth(client, message: Message):
    t = random.choice(truths)
    await message.reply(f"🧠 Truth:\n\n{t}\n\n_By: @KRIYANSH_CHOUDHARY_")
