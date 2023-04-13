import os

import pytest
from one_api_sid_sdk.models import Quote, Movie
from one_api_sid_sdk.client import OneApiClient
from .utils import requires_api_key


def test_quote_from_data():
    quote_data = {
        "_id": "5cd96e05de30eff6ebcce0b6",
        "dialog": "I am Gandalf the White.",
        "movie": "5cd95395de30eff6ebccde5c",
        "character": "5cd99d4bde30eff6ebccfb54"
    }

    quote = Quote.from_data(quote_data)

    assert quote.id == "5cd96e05de30eff6ebcce0b6"
    assert quote.dialog == "I am Gandalf the White."
    assert quote.movie == "5cd95395de30eff6ebccde5c"
    assert quote.character == "5cd99d4bde30eff6ebccfb54"


def test_quote_from_json():
    quote_json = '''
    {
        "_id": "5cd96e05de30eff6ebcce0b6",
        "dialog": "I am Gandalf the White.",
        "movie": "5cd95395de30eff6ebccde5c",
        "character": "5cd99d4bde30eff6ebccfb54"
    }
    '''

    quote = Quote.from_json(quote_json)

    assert quote.id == "5cd96e05de30eff6ebcce0b6"
    assert quote.dialog == "I am Gandalf the White."
    assert quote.movie == "5cd95395de30eff6ebccde5c"
    assert quote.character == "5cd99d4bde30eff6ebccfb54"


@requires_api_key
def test_the_one_api_get_all_quotes():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    quotes = api.get_all(Quote, parent_model=Movie, parent_id=movie_id)

    assert len(quotes) > 0
    assert isinstance(quotes[0], Quote)