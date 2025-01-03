from __future__ import annotations

import re
from typing import List

from constant.excel import ActivityType
from constant.notion import ACTIVITY_REQUIRED_PROPERTIES, PropertyValuePattern


def check_activities_time(
    activities: List[list], timeline_start_limit: str, timeline_end_limit: str
) -> None:
    """Check the time info in data is correct or not.

    :param activities: notion database activity data
    :param timeline_start_limit: activities timeline must later than it
    :param timeline_end_limit: activities timeline must earlier than it

    :return: None
    """
    for daily_activities in activities:
        for activity in daily_activities:
            if not (timeline_start_limit < activity["start_at"] <= timeline_end_limit):
                print(
                    f"Activity: {activity}. Its start_at is not in {timeline_start_limit} to {timeline_end_limit}."
                )
                raise Exception("Activity start_at is not vaild.")
            if not (timeline_start_limit < activity["end_at"] <= timeline_end_limit):
                print(
                    f"Activity: {activity}. Its end_at is not in {timeline_start_limit} to {timeline_end_limit}."
                )
                raise Exception("Activity end_at is not vaild.")


def check_activities_required_fields(activities: List[list]) -> None:
    """Check activities required fields is correct or not.

    :param activities: notion database activity data

    :return: None
    """
    for daily_activities in activities:
        for activity in daily_activities:
            for property_name, property_value in activity.items():
                if property_name in ACTIVITY_REQUIRED_PROPERTIES:
                    if property_value == "":
                        print(f"Activity: {activity}. Its {property_name} is empty.")
                        raise Exception("Activity required field is empty.")

                if property_name in PropertyValuePattern.__members__:
                    if (
                        re.fullmatch(PropertyValuePattern[property_name].value, property_value)
                        is None
                    ):
                        print(
                            f"Activity: {activity}. Its {property_name} is {property_value}, it's not vaild."
                        )
                        raise Exception(f"Activity's {property_name} is not valid.")


def check_options_in_activities_data_is_vaild(activities: List[list]) -> None:
    """Check options in activities data is vaild or not.

    :param activities: notion database activity data

    :return: None
    """
    avalible_activity_types = [activity_type.value for activity_type in ActivityType]
    for daily_activities in activities:
        for activity in daily_activities:
            if activity["type"] not in avalible_activity_types:
                print(f"Activity: {activity}. Its type is {activity['type']}, it's not vaild.")
                raise Exception("Activity's type is not valid.")
