import os

# Telegram API
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# MongoDB
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# String Session
STRING_SESSION = os.getenv("STRING_SESSION", "")

# Log Group
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))

# Bot Information
BOT_NAME = "Iqra Music Bot"
BOT_USERNAME = "YourBotUsername"

# Support
SUPPORT_CHAT = "YourSupportGroup"
UPDATES_CHANNEL = "YourUpdatesChannel"
