import src.function_log.main
from src.function_log.main import *

__all__ = (main.__all__)

VERSION = (0, 0, 1)


# def get_version():
#     if isinstance(VERSION[-1], basestring):
#         return '.'.join(map(str, VERSION[:-1])) + VERSION[-1]
#     return '.'.join(map(str, VERSION))
#
# __version__ = get_version()