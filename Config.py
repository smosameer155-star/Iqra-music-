
import os

# Telegram API
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH")

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Log Group
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001234567890"))

# Session String
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Bot Name
BOT_NAME = "Iqra Music & Video Bot"
