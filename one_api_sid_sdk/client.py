from typing import Type, List
import requests
from .models.base_model import BaseModel
from .models.one_api_response import OneApiResponse


class OneApiClient:
    BASE_URL = "https://the-one-api.dev/v2/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_all(self, model: Type[BaseModel]) -> List[BaseModel]:
        endpoint = self._get_endpoint(model)
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            one_api_response = OneApiResponse(response_data, model)
            return one_api_response.docs
        else:
            response.raise_for_status()

    def _get_endpoint(self, model: Type[BaseModel]) -> str:
        model_name = model.__name__.lower()
        return f"{model_name}"
