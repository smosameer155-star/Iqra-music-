from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "IqraMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   IQRA MUSIC BOT STARTED")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    app.start()
    print("Bot is now online...")
    idle()
    app.stop()

    print("Bot stopped.")
