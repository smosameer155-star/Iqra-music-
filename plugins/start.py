from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import (
    BOT_NAME,
    SUPPORT_CHAT,
    UPDATES_CHANNEL,
)


@Client.on_message(filters.command("start"))
async def start_command(client, message):

    user = message.from_user.mention

    text = f"""
👋 Hello {user}

🎵 Welcome to {BOT_NAME}

✨ Features:
➤ YouTube Music
➤ YouTube Video
➤ Telegram Audio
➤ Telegram Video
➤ Voice Chat Streaming
➤ Queue System
➤ High Quality Playback

👇 Choose an option below.
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕ Add Me", url="https://t.me/YourBotUsername?startgroup=true")
            ],
            [
                InlineKeyboardButton("📚 Help", callback_data="help"),
                InlineKeyboardButton("🎵 Commands", callback_data="commands"),
            ],
            [
                InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("💬 Support", url=f"https://t.me/{SUPPORT_CHAT}"),
            ],
            [
                InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/YourUsername")
            ]
        ]
    )

    await message.reply_text(
        text,
        reply_markup=buttons,
        disable_web_page_preview=True,
    )
