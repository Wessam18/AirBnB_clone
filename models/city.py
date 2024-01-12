#!/usr/bin/pyhon3
"""city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class inherit of BaseModel"""
    state_id = ""
    name = ""
