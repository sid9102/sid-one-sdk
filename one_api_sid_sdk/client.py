import requests


class OneApiClient:
    BASE_URL = "https://the-one-api.dev/v2/"

    def __init__(self, api_key: str):
        self.api_key = api_key
