from __future__ import annotations
from typing import TYPE_CHECKING, List


def check_activities_time(activities: List[list], timeline_start_limit: str, timeline_end_limit: str) -> None:
    """ Check the time info in data is correct or not.

    :param activities: notion database activity data
    :param timeline_start_limit: activities timeline must later than it
    :param timeline_end_limit: activities timeline must earlier than it

    :return: None
    """
    for daily_activities in activities:
        for activity in daily_activities:
            if not (timeline_start_limit < activity["start_at"] <= timeline_end_limit):
                print(f"Activity: {activity}. Its start_at is not in {timeline_start_limit} to {timeline_end_limit}.")
                raise Exception("Activity start_at is not vaild.")
            if not (timeline_start_limit < activity["end_at"] <= timeline_end_limit):
                print(f"Activity: {activity}. Its end_at is not in {timeline_start_limit} to {timeline_end_limit}.")
                raise Exception("Activity end_at is not vaild.")