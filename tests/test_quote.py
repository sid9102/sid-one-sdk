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


@requires_api_key
def test_the_one_api_get_quotes_with_limit():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    quotes = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, limit=3)

    assert len(quotes) == 3
    assert isinstance(quotes[0], Quote)


def test_the_one_api_get_quotes_with_page():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    quotes_page_1 = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, page=1, limit=1)
    quotes_page_2 = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, page=2, limit=1)

    assert len(quotes_page_1) > 0
    assert len(quotes_page_2) > 0
    assert quotes_page_1[0].id != quotes_page_2[0].id


@requires_api_key
def test_the_one_api_get_quotes_with_offset():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    quotes_offset_0 = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, offset=0)
    quotes_offset_1 = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, offset=1)

    assert len(quotes_offset_0) > 0
    assert len(quotes_offset_1) > 0
    assert quotes_offset_0[0].id != quotes_offset_1[0].id

@requires_api_key
def test_the_one_api_get_quotes_with_sort():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    quotes_sorted_asc = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, sort="dialog", ascending=True)
    quotes_sorted_desc = api.get_all(Quote, parent_model=Movie, parent_id=movie_id, sort="dialog", ascending=False)

    assert len(quotes_sorted_asc) > 0
    assert len(quotes_sorted_desc) > 0
    assert quotes_sorted_asc[0].id != quotes_sorted_desc[0].id


@requires_api_key
def test_the_one_api_get_quote_instance():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    quote_id = "5cd96e05de30eff6ebcced61"
    quote = api.get_instance(Quote, quote_id)

    assert quote is not None
    assert isinstance(quote, Quote)
    assert quote.id == quote_id


@requires_api_key
def test_the_one_api_get_quote_instance_not_found():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    quote_id = "non_existent_quote_id"
    quote = api.get_instance(Quote, quote_id)

    assert quote is None
