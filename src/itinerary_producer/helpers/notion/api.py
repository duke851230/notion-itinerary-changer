from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

import requests

from configer import configer


def get_databases_data(database_id: str) -> dict:
    token: str = configer.notion.TOKEN

    header_payload: dict = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    url: str = f"https://api.notion.com/v1/databases/{database_id}/query"

    response = requests.request('POST', url, headers=header_payload)
    data: dict = response.json()

    return data