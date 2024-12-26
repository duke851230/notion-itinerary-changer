from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


def exchange_place_with_key_and_value(data: dict) -> dict:
    return {v: k for k, v in data.items()}
