from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from enum import Enum


class ColorMap(Enum):
    blue = "00CCFFFF"
    yellow = "00FFFF99"
    beige = "00FFFFCC"
    purple = "00CCCCFF"
    green = "00CCFFCC"
    orange = "00FFCC99"
    pink = "00FF99CC"
    gray = "DDDDDD"

