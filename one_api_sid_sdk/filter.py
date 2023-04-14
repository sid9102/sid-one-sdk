from enum import Enum
from typing import Union, List


class FilterOperation(Enum):
    MATCH = "="
    NOT_MATCH = "!="
    INCLUDE = "="
    EXCLUDE = "!="
    EXISTS = "EXISTS"
    NOT_EXISTS = "NOT_EXISTS"
    REGEX = "REGEX"
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="


class Filter:
    def __init__(self, field: str, operation: FilterOperation, value: Union[str, List[str]]):
        self.field = field
        self.operation = operation
        self.value = value

    def to_suffix(self) -> str:
        if self.operation in [FilterOperation.EXISTS, FilterOperation.NOT_EXISTS]:
            return f"{self.field}" if self.operation == FilterOperation.EXISTS else f"!{self.field}"
        elif self.operation == FilterOperation.REGEX:
            return f"{self.field}={self.value}"
        elif self.operation == FilterOperation.INCLUDE:
            return f"{self.field}={','.join(self.value)}"
        elif self.operation == FilterOperation.EXCLUDE:
            return f"{self.field}!={','.join(self.value)}"
        else:
            value = ','.join(self.value) if isinstance(self.value, list) else self.value
            return f"{self.field}{self.operation.value}{value}"
