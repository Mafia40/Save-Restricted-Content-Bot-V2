# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21353303"))
API_HASH = getenv("API_HASH", "f4197ef1b8f228dd5762ef465fc3b910")
BOT_TOKEN = getenv("BOT_TOKEN", "7964026673:AAG_QGKYAUClTzCi41nAgJ-NEKBZeENkCn0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6030113916").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saovishal:<#T@654321@sa1>@cluster0.0d5dk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002347158080")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002359200771"))
