
from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def ajg(client):
    try:
        await client.join_chat("obrolansuar")
        await client.join_chat("StoreKarman")
        await client.join_chat("RuangGabutArman")
    except BaseException:
        pass
