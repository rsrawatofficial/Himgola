"""
from os import getenv


API_ID = int(getenv("API_ID", "27900743"))
API_HASH = getenv("API_HASH", "ebb06ea8d41420e60b29140dcee902fc")
BOT_TOKEN = getenv("BOT_TOKEN", "7609528498:AAGqcl_h-Cygc4v_oiXqD4cbp-yGypVcakY")
OWNER_ID = int(getenv("OWNER_ID", "7804396225"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7804396225").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://rsrawat9521:bjdchdgcyuwhckhdcwkgckwyd@cluster0.pfie6h0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002566364060"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002566364060"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27900743"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8003649544:AAGoiThVN8KLJyKGsGf1BcfTsjDTrSmjFR8")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7804396225"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7804396225").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002566364060"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002456765218"))

