
from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *

async def join(client):
    try:
        await client.join_chat("Zorxd")
        await client.join_chat("BigNomame")
    except BaseException:
        pass
