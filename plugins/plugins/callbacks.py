from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


@Client.on_callback_query(filters.regex("back"))
async def back_callback(client, callback_query):

    user = callback_query.from_user.mention

    text = f"""
👋 Hello {user}

🎵 Welcome to IQRA MUSIC BOT

✨ Features

🎧 YouTube Music
🎬 YouTube Video
📂 Telegram Audio
📹 Telegram Video
📜 Queue System
⚡ Fast Streaming

Choose an option below.
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me",
                    url="https://t.me/YourBotUsername?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    "📚 Help",
                    callback_data="help",
                ),
                InlineKeyboardButton(
                    "🎵 Commands",
                    callback_data="commands",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url="https://t.me/YourUpdatesChannel",
                ),
                InlineKeyboardButton(
                    "💬 Support",
                    url="https://t.me/YourSupportGroup",
                ),
            ],
            [
                InlineKeyboardButton(
                    "👨‍💻 Developer",
                    url="https://t.me/YourUsername",
                )
            ],
        ]
    )

    await callback_query.message.edit_text(
        text,
        reply_markup=buttons,
    )
