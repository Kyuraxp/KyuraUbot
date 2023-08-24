from pyrogram.types import InlineKeyboardButton, WebAppInfo
from Ubot.modules.basic import cmds, CMD_HELP
class Data:

    basic = CMD_HELP
    
    num_basic_modules = len(basic)

    text_help_menu = (
        f"**• Help Menu **\n**• Modules: <code>{num_basic_modules} Modules</code>\n**• prefixes **: `None`"
    )
    reopen = [[InlineKeyboardButton("Open", callback_data="reopen")]]
