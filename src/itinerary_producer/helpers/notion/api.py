from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

import requests

from configer import configer


def get_database_data(database_id: str) -> dict:
    """ Get database data in notion.

    :param database_id: database's id, e.g. "6b46bb53911045bb92f2298aww1c13b3"

    :return: data of database
    """
    token: str = configer.notion.TOKEN
    header_payload: dict = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    url: str = f"https://api.notion.com/v1/databases/{database_id}/query"

    response = requests.request('POST', url, headers=header_payload)
    data: dict = response.json()
    # print(f"data: {data}")

    return data