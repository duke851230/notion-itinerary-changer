from __future__ import annotations
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

import os, sys
import toml
from pydantic import BaseModel


def get_config_path() -> str:
    CONFIG_DIRECTORY_NAME: str = "config"
    CONFIG_FILE_NAME: str = "config.toml"

    current_file_path: str = os.path.abspath(sys.modules["__main__"].__file__)
    current_file_directory: str = os.path.dirname(current_file_path)

    return os.path.join(current_file_directory, CONFIG_DIRECTORY_NAME, CONFIG_FILE_NAME)

def read_toml_data(file_path: str) -> dict:
    config_data: dict = {}

    try:
        with open(file_path, "r") as f:
            config_data = toml.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"file: '{file_path}' doesn't exist")
    
    return config_data

def initialize_config_model(config_class: BaseModel, toml_keyword: str) -> BaseModel:
    """ Get toml config by keyword, and set every setting value into class attributes.

    :param config_class: the config model which must inherited from BaseModel
    :param toml_keyword: block name in toml file

    :return: config class
    """
    config_data: dict = read_toml_data(
        file_path=get_config_path()     
    )

    try:
        config: dict = config_data[toml_keyword]
    except KeyError:
        raise KeyError(f"config section {toml_keyword} not found")

    return config_class(**config)
        

class NotionConfig(BaseModel, extra="forbid"):
    TOKEN: str
    DATABASE_ID: str


class ExcelConfig(BaseModel, extra="forbid"):
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
