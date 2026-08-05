from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(filters.regex("help"))
async def help_callback(client, callback_query):

    text = """
📚 **IQRA MUSIC BOT HELP**

🎵 Music Commands
/play <song name>
/pause
/resume
/skip
/stop

🎬 Video Commands
/vplay <video name>

/playlist
/queue

👮 Admin Commands
/end
/restart

More features will be added soon.
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⬅ Back", callback_data="back")
            ]
        ]
    )

    await callback_query.message.edit_text(
        text,
        reply_markup=buttons
    )
