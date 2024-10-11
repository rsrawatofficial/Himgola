#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE


import os
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, SUDO_USERS, MONGO_URL, CHANNEL_ID, PREMIUM_LOGS  # Directly import required variables

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
# If AUTH_USERS is available in os.environ, handle it as a string and convert to a list of integers
AUTH_USERS = [int(chat) for chat in os.getenv("AUTH_USERS", "").split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

if __name__ == "__main__":
    bot = Client(
        "doms_extra_bot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        sleep_threshold=20,
        plugins=plugins,
        workers=50
    )
    
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) LUCIFERBANKER --->")
        await idle()

    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped--->")

