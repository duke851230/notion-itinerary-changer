from __future__ import annotations
from typing import (
    TYPE_CHECKING, List, Optional
)

if TYPE_CHECKING:
    pass

import os
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl import Workbook

from configer import configer
from helpers.excel.sheet import (
    set_timeline_in_sheet,
)


file_path: str = os.path.join(configer.excel.EXCEL_BASIC_DIR, "test.xlsx")

wb: Workbook = Workbook()
sheet: Worksheet = wb.active

set_timeline_in_sheet(sheet, {2: "test"})

wb.save(file_path)
