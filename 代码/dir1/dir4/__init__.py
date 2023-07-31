position = __path__[0]
__path__ = [position, position + '/dir5']

from .e import E9, E10
from .f import F11, F12
from ..dir2.dir3 import D7
