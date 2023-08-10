from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from enum import Enum


class PropertyType(Enum):
    name = "title"
    date = "date"
    note = "rich_text"
    end_at = "rich_text"
    start_at = "rich_text"
    type = "select"
