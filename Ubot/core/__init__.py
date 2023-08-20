
from .ai import *
from .data import *
from .func import *
from .inline import *
from .lgs import *
from .what import *
from .filter import *
from .constants import *
from Ubot.core.db.mongo import db


prefix = db.get("core.main", "prefix", ".")
