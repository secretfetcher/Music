import time

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram.raw.functions.messages import SendReaction
from pyrogram.raw.types import ReactionEmoji

import config
from ShrutiMusic import app
from ShrutiMusic.misc import _boot_
from ShrutiMusic.utils.database import add_served_chat, add_served_user
from ShrutiMusic.utils import bot_sys_stats
from ShrutiMusic.utils.decorators.language import LanguageStart
from ShrutiMusic.utils.formatters import get_readable_time
from ShrutiMusic.utils.inline import private_panel, start_panel
from config import BANNED_USERS


# 🔥 Auto Reaction
async def auto_react(client, message):
    try:
        await client.invoke(
            SendReaction(
                peer=await client.resolve_peer(message.chat.id),
                msg_id=message.id,
                reaction=[ReactionEmoji(emoticon="🔥")]
            )
        )
    except:
        pass


# ================= PRIVATE START =================
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # ❤️ Auto reaction
    await auto_react(client, message)

    out = private_panel(_)
    UP, CPU, RAM, DISK = await bot_sys_stats()

    caption = f"""
✨ **WELCOME TO PREMIUM MUSIC BOT** ✨

👤 User: {message.from_user.mention}
🤖 Bot: {app.mention}

🔥 Features:
➤ Fast Music Streaming
➤ 24/7 Active
➤ Premium UI

🎧 Try: /play song name
"""

    try:
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(out),
        )
    except:
        await message.reply_text(caption)


# ================= GROUP START =================
@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):

    await auto_react(client, message)

    out = start_panel(_)
    uptime = int(time.time() - _boot_)

    text = f"""
🔥 {app.mention} is running!

⏱ Uptime: {get_readable_time(uptime)}
🎧 Use /play to start music
"""

    try:
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=text,
            reply_markup=InlineKeyboardMarkup(out),
        )
    except:
        await message.reply_text(text)

    return await add_served_chat(message.chat.id)


# ================= WELCOME =================
@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        if member.id == app.id:
            out = start_panel("en")

            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption="🎉 Thanks for adding me!\n\n👉 Use /play to start music",
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    "🎉 Thanks for adding me!\n\n👉 Use /play to start music"
                )

            await add_served_chat(message.chat.id)
