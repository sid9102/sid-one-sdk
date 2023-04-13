from typing import List, TypeVar, Generic, Type

from .base_model import BaseModel

T = TypeVar('T', bound='BaseModel')


class OneApiResponse(Generic[T]):
    def __init__(self, response_data: dict, data_cls: Type[BaseModel]):
        self.docs = [data_cls.from_data(data) for data in response_data["docs"]]
        self.total = response_data["total"]
        self.limit = response_data["limit"]
        self.offset = response_data["offset"]
        self.page = response_data["page"]
        self.pages = response_data["pages"]
