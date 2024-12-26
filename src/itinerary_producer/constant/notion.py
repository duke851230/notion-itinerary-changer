from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from enum import Enum

ACTIVITY_REQUIRED_PROPERTIES: list = ["name", "date", "start_at", "end_at", "type"]


class PropertyType(Enum):
    name = "title"
    date = "date"
    note = "rich_text"
    end_at = "rich_text"
    start_at = "rich_text"
    type = "select"


class PropertyValuePattern(Enum):
    type = ".+"
    date = r"(\d+)-(\d+)-(\d+)"  # e.g. 2023-01-01
    start_at = r"(\d{2}:\d{2})"  # e.g. 15:30
    end_at = r"(\d{2}:\d{2})"  # e.g. 15:30
