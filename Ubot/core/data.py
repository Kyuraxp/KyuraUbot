from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Ubot.modules.basic import cmds, CMD_HELP
class Data:

    basic = CMD_HELP
    
    text_help_menu = (
        f"**•Help Menu**\n**•  Modules: <code>{len(modules,basic)} Modules</code>\n**•refixes** : `None`"
    )
    reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
