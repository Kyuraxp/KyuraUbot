# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
import random
import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio 
from gc import get_objects

from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from Ubot.core import *
from Ubot.core.db import *
from pyrogram.raw.core.primitives.vector import *
from pyrogram.raw.functions import Ping
from ubotlibs import BOT_VER
import config
from Ubot import CMD_HELP, StartTime, app, ids, cmds


WHITE = [450653634, 1909700822]

BLACK = [450653634, 1909700822]


def support():
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_help"),
        ],
    ]
    return buttons

async def get_readable_time(seconds: int) -> str:    
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    

async def alive_function(message, answers):
    status = ""
    if message._client.me.id in BLACK:
        status = "[𝘖𝘸𝘯𝘦𝘳]"
    elif message._client.me.id == OWNER_ID:
        status = "[𝘈𝘥𝘮𝘪𝘯𝘴]"
    else:
        status = "[user]"
    start = datetime.now()
    buttons = support()
    ex = await message._client.get_me()
    remaining_days = "None"
    user = len(ids)
    await message._client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    msg = (
        f"<b>Pepek</b>\n"
        f"<b> Status: Active {status} </b>\n"
        f"    <b> expired:</b> <code>{remaining_days}</code>\n"
        f"    <b> ping_ubot:</b> <code>{ping} ms</code>\n"
        f"    <b> peer_ubot:</b> <code>{user}</code>\n"
        f"    <b> uptime_ubot:</b> <code>{uptime}</code>\n")
    answers.append(
        InlineQueryResultArticle(
            title="alive",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(buttons)))
    return answers



async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
# @inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        answerss = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            m = [obj for obj in get_objects() if id(obj) == int(query.query.split(None, 1)[1])][0]
            answerss = await alive_function(m, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)

    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
      
