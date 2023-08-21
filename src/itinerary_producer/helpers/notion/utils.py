from __future__ import annotations
from typing import (
    TYPE_CHECKING, Callable, Dict, List,
)

if TYPE_CHECKING:
    pass

import re

from configer import configer
from constant.notion import PropertyType, PropertyValuePattern
from helpers.notion import property
from helpers.notion.api import (
    get_database_data,
)


def get_daily_activities() -> List[list]:
    """ Get everyday activities in schedule.

    The daily activities will be sorted by start_at field.
    One of inner list is activities in one day, one dict in inner list is a activity.

    :return: everyday activities

    :return example:
    [
        [
           {'date': '2023-09-30', 'name': '去程飛機', 'note': '', 'type': '交通', 'end_at': '11:30', 'start_at': '08:00'},
            ...
        ],
        ...
    ]
    """
    data = get_database_data(configer.notion.DATABASE_ID)

    temp_daily_data: Dict[str, list] = {}
    for card in data["results"]:
        card_properties: Dict[str, dict] = card["properties"]

        card_info: dict = {}
        for field_name, info in card_properties.items():
            lower_field_name: str = field_name.lower()
            if lower_field_name in PropertyType.__members__:
                property_type: str = PropertyType[lower_field_name].value
                method: Callable = getattr(property, f"get_{property_type}")
                card_info[lower_field_name] = method(info)
        
        cur_day: str = card_info[PropertyType.date.name]
        if cur_day not in temp_daily_data:
            temp_daily_data[cur_day] = []
        
        if verify_activity_info(card_info):
            temp_daily_data[cur_day].append(card_info)

    days: List[str] = list(temp_daily_data.keys())
    days.sort()
    daily_activities: List[list] = [temp_daily_data[i] for i in days]

    daily_activities = sort_daily_activities(daily_activities)
    # print(f"daily_activities: {daily_activities}")
    return daily_activities

def sort_daily_activities(daily_activities: List[list]) -> List[list]:
    """ Sort every one day activities.

    :param daily_activities: all activities which are grouped by day in itinerary

    :return: sorted activities
    """
    SORTED_BY = "start_at"

    sorted_data: List[list] = []
    for today_activities in daily_activities:
        sorted_data.append(
            sorted(
                today_activities,
                key=lambda x: x[SORTED_BY]
            )
        )
    
    return sorted_data

def verify_activity_info(activity: dict) -> bool:
    """ Check activity properties whether correct or not.

    :param activity: one acitivity's properties

    :return: is valid or not
    """
    for k, v in activity.items():
        if k not in PropertyValuePattern.__members__:
            continue

        if re.fullmatch(PropertyValuePattern[k].value, v) is None:
            print(k, v)
            return False

    return True