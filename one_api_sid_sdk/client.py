from typing import Type, List, Optional
import requests
from .models.base_model import BaseModel
from .models.one_api_response import OneApiResponse


def _get_endpoint(model: Type[BaseModel],
                  parent_model: Optional[Type[BaseModel]] = None,
                  parent_id: str = None) -> str:
    model_name = model.__name__.lower()
    if parent_model is not None and parent_id is not None:
        parent_model_name = parent_model.__name__.lower()
        return f"{parent_model_name}/{parent_id}/{model_name}"
    return f"{model_name}"


class OneApiClient:
    BASE_URL = "https://the-one-api.dev/v2/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_all(self,
                model: Type[BaseModel],
                parent_model: Optional[Type[BaseModel]] = None,
                parent_id: str = None) -> List[BaseModel]:
        endpoint = _get_endpoint(model, parent_model, parent_id)
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            one_api_response = OneApiResponse(response_data, model)
            return one_api_response.docs
        else:
            response.raise_for_status()
