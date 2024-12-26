from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    pass

import os
import sys

import toml
from pydantic import BaseModel  # type: ignore


def get_config_path() -> str:
    """Get absolute path of config file.

    :return: absolute path of config file
    """
    CONFIG_DIRECTORY_NAME: str = "config"
    CONFIG_FILE_NAME: str = "config.toml"

    execution_relative_path: Optional[str] = sys.modules["__main__"].__file__
    if execution_relative_path is None:
        raise Exception("Can't find execution path")

    file_absolute_path: str = os.path.abspath(execution_relative_path)
    file_directory_path: str = os.path.dirname(file_absolute_path)

    return os.path.join(file_directory_path, CONFIG_DIRECTORY_NAME, CONFIG_FILE_NAME)


def read_toml_data(file_path: str) -> dict:
    config_data: dict = {}

    try:
        with open(file_path, "r") as f:
            config_data = toml.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"file: '{file_path}' doesn't exist")

    return config_data


def initialize_config_model(config_class: BaseModel, toml_keyword: str) -> BaseModel:
    """Filter toml config by keyword, and set settings value into class attributes.

    :param config_class: the config model which must inherited from BaseModel
    :param toml_keyword: block name in toml file

    :return: config class
    """
    config_data: dict = read_toml_data(file_path=get_config_path())

    try:
        config: dict = config_data[toml_keyword]
    except KeyError:
        raise KeyError(f"config section {toml_keyword} not found")

    return config_class(**config)


class NotionConfig(BaseModel):
    TOKEN: str
    DATABASE_ID: str


class ExcelConfig(BaseModel):
    EXCEL_BASIC_DIR: str
    FILE_NAME: str
    SCHEDULE_TIMELINE_START_AT: str
    SCHEDULE_TIMELINE_END_AT: str
    SCHEDULE_TIMELINE_INTERVAL: int
    MINIMAL_INTERVAL: int


class Configer(BaseModel):
    notion: NotionConfig = initialize_config_model(config_class=NotionConfig, toml_keyword="notion")
    excel: ExcelConfig = initialize_config_model(config_class=ExcelConfig, toml_keyword="excel")


configer: Configer = Configer()
