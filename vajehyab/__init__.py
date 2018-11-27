import sys
from logging import logging, NullHandler


logger = logging.getLogger(__name__)
handler = logger.addHandler(NullHandler)
logger.addHandler(handler)

from .core import *
