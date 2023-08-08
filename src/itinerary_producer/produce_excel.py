from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

import os
from datetime import datetime
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl import Workbook

from configer import configer
from helpers.excel.sheet import (
    initialize_sheet,
    set_timeline_in_sheet,
    insert_activities_to_sheet,
)
from helpers.excel.utils import (
    get_timeline_data,
)
from helpers.notion.utils import (
    get_daily_activities,
)


FILE_PATH: str = os.path.join(
    configer.excel.EXCEL_BASIC_DIR,
    configer.excel.FILE_NAME
)

def produce_schedule_excel(file_path: str) -> None:
    wb: Workbook = Workbook()
    sheet: Worksheet = wb.active

    initialize_sheet(sheet=sheet)

    pre_timeline, timeline = get_timeline_data(
        start_at=datetime(9999, 1, 1, 8, 00),
        end_at=datetime(9999, 1, 1, 21, 30),
        start_row_number=3,
        time_interval=30
    )
    set_timeline_in_sheet(
        sheet=sheet,
        column="A",
        name="起始時間",
        name_row_number=2,
        timeline_data=pre_timeline
    )
    set_timeline_in_sheet(
        sheet=sheet,
        column="B",
        name="結束時間",
        name_row_number=2,
        timeline_data=timeline
    )

    insert_activities_to_sheet(
        sheet=sheet,
        activities=get_daily_activities(),
        timeline=timeline,
        start_column="C"
    )

    wb.save(file_path)


if __name__ == "__main__":
    produce_schedule_excel(FILE_PATH)
