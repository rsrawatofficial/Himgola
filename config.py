"""
from os import getenv


API_ID = int(getenv("API_ID", "20736921"))
API_HASH = getenv("API_HASH", "42b34442e52dc3e07b3e0783389be8cb")
BOT_TOKEN = getenv("BOT_TOKEN", "8015663864:AAGLRoTMXkj9Ndq4PL7oKLo0AtaYT68rxCM")
OWNER_ID = int(getenv("OWNER_ID", "1366730834"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1366730834").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://creatorar30:fdINvMPYXYwUyHdq@cluster0.pbaou.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002456765218"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002373511813"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "20736921"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8015663864:AAGLRoTMXkj9Ndq4PL7oKLo0AtaYT68rxCM")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "1366730834"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1366730834").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002319636950"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002456765218"))

