from abc import ABC
import json
from typing import TypeVar, Dict, Type

T = TypeVar('T', bound='BaseModel')


class BaseModel(ABC):

    @classmethod
    def from_data(cls: Type[T], data: Dict) -> T:
        return cls(data)

    @classmethod
    def from_json(cls: Type[T], json_str: str) -> T:
        data = json.loads(json_str)
        return cls.from_data(data)
