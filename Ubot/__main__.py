import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle
from pyrogram.errors import RPCError
from uvloop import install
from ubotlibs import *
from Ubot import BOTLOG_CHATID, aiosession, bot1, bots, app, ids, LOOP, event_loop
from platform import python_version as py
from Ubot.logging import LOGGER
from pyrogram import __version__ as pyro
import sqlite3
from Ubot.modules import ALL_MODULES
from Ubot.core.db import *
from config import SUPPORT, CHANNEL
import os
from dotenv import load_dotenv
from pyrogram.errors import RPCError

BOT_VER ="8.1.0"

MSG_BOT = """
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**New Ubot Actived ✅**
**Phython**: `{}`
**Pyrogram**: `{}`
**User**: `{}`
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

MSG_ON = """
**New Ubot Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Ubot").info("Memulai Ubot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await buat_log(bot)
            botlog_chat_id = await get_botlog(user_id)
            LOGGER("Ubot").info("Startup Completed")
            LOGGER("√").info(f"Started as {ex.first_name} | {ex.id} ")
            await join(bot)
            user = len(ids)
#            await bot.send_message(botlog_chat_id, MSG_ON.format(BOT_VER, py(), pyro))
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
    
    await app.send_message(SUPPORT, MSG_BOT.format(py(), pyro, user))
    await idle()
    await aiosession.close()

    


              

if __name__ == "__main__":
    LOGGER("Ubot").info("Starting  Ubot")
    install()
#    LOOP.run_until_complete(main())
    event_loop.run_until_complete(main())
