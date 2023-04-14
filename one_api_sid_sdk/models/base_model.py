import json
from abc import ABC
from typing import TypeVar, Dict, Type

T = TypeVar('T', bound='BaseModel')


class BaseModel(ABC):

    def __init__(self):
        self.id = None

    @classmethod
    def from_data(cls: Type[T], data: Dict) -> T:
        return cls(data)

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        data = json.loads(json_str)
        return cls.from_data(data)
