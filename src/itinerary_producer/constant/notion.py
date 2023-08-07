from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from enum import Enum


class PropertyType(Enum):
    name = "title"
    day = "rich_text"
    place = "rich_text"
    end_at = "date"
    start_at = "date"
