import asyncio
import logging

from pyrogram import Client, filters
from pyrogram.types import Message

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
)

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create Bot Client
app = Client(
    "IqraMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        "👋 Welcome to Iqra Music & Video Bot!\n\n"
        "🎵 YouTube Music\n"
        "🎬 YouTube Video\n"
        "📂 Telegram Audio & Video\n"
        "🎧 Voice Chat Streaming\n\n"
        "Use /help to see all commands."
    )


@app.on_message(filters.command("help"))
async def help_command(_, message: Message):
    await message.reply_text(
        "📖 Commands\n\n"
        "/play - Play Music or Video\n"
        "/pause - Pause Stream\n"
        "/resume - Resume Stream\n"
        "/skip - Skip Current Track\n"
        "/stop - Stop Streaming"
    )


async def main():
    await app.start()
    print("✅ Iqra Music Bot Started Successfully!")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
