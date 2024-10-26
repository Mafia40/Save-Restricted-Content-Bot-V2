# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21353303"))
API_HASH = getenv("API_HASH", "f4197ef1b8f228dd5762ef465fc3b910")
BOT_TOKEN = getenv("BOT_TOKEN", "8162565946:AAHRA2PeM7Zy9C2yFw9p4P7U6ue7Xj7xn8o")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6030113916").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saovishal9876:SGxuSobdqiG3DERz@cluster0.cn1zo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002347158080")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002359200771"))
