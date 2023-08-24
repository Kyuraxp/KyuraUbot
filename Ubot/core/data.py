from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Ubot.modules.basic import cmds, CMD_HELP

class Data:
    
   num_basic_modules = len(CMD_HELP)

   text_help_menu = (
        f"**• Help Menu **\n**• Modules: <code>{num_basic_modules} Modules</code>\n**• prefixes **: `{cmds}`"
    )
   reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
