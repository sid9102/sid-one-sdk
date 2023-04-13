import os

import pytest
from one_api_sid_sdk.models import Movie
from one_api_sid_sdk.client import OneApiClient
from .utils import requires_api_key


def test_movie_from_data():
    movie_data = {
        "_id": "5cd95395de30eff6ebccde5c",
        "name": "The Fellowship of the Ring",
        "runtimeInMinutes": 178,
        "budgetInMillions": 93,
        "boxOfficeRevenueInMillions": 871.5,
        "academyAwardNominations": 13,
        "academyAwardWins": 4,
        "rottenTomatoesScore": 91
    }

    movie = Movie.from_data(movie_data)

    assert movie.id == "5cd95395de30eff6ebccde5c"
    assert movie.name == "The Fellowship of the Ring"
    assert movie.runtime_in_minutes == 178
    assert movie.budget_in_millions == 93
    assert movie.box_office_revenue_in_millions == 871.5
    assert movie.academy_award_nominations == 13
    assert movie.academy_award_wins == 4
    assert movie.rotten_tomatoes_score == 91


def test_movie_from_json():
    movie_json = '''
    {
        "_id": "5cd95395de30eff6ebccde5c",
        "name": "The Fellowship of the Ring",
        "runtimeInMinutes": 178,
        "budgetInMillions": 93,
        "boxOfficeRevenueInMillions": 871.5,
        "academyAwardNominations": 13,
        "academyAwardWins": 4,
        "rottenTomatoesScore": 91
    }
    '''

    movie = Movie.from_json(movie_json)

    assert movie.id == "5cd95395de30eff6ebccde5c"
    assert movie.name == "The Fellowship of the Ring"
    assert movie.runtime_in_minutes == 178
    assert movie.budget_in_millions == 93
    assert movie.box_office_revenue_in_millions == 871.5
    assert movie.academy_award_nominations == 13
    assert movie.academy_award_wins == 4
    assert movie.rotten_tomatoes_score == 91


@requires_api_key
def test_the_one_api_get_all_movies():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movies = api.get_all(Movie)

    assert len(movies) > 0
    assert isinstance(movies[0], Movie)


@requires_api_key
def test_the_one_api_get_movies_with_limit():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movies = api.get_all(Movie, limit=3)

    assert len(movies) == 3
    assert isinstance(movies[0], Movie)


@requires_api_key
def test_the_one_api_get_movies_with_page():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movies_page_1 = api.get_all(Movie, page=1, limit=1)
    movies_page_2 = api.get_all(Movie, page=2, limit=1)

    assert len(movies_page_1) > 0
    assert len(movies_page_2) > 0
    assert movies_page_1[0].id != movies_page_2[0].id

@requires_api_key
def test_the_one_api_get_movies_with_offset():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movies_offset_0 = api.get_all(Movie, offset=0)
    movies_offset_1 = api.get_all(Movie, offset=1)

    assert len(movies_offset_0) > 0
    assert len(movies_offset_1) > 0
    assert movies_offset_0[0].id != movies_offset_1[0].id


@requires_api_key
def test_the_one_api_get_movie_instance():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "5cd95395de30eff6ebccde5c"
    movie = api.get_instance(Movie, movie_id)

    assert movie is not None
    assert isinstance(movie, Movie)
    assert movie.id == movie_id


@requires_api_key
def test_the_one_api_get_movie_instance_not_found():
    with open("API_KEY", "r") as api_key_file:
        api_key = api_key_file.read().strip()

    api = OneApiClient(api_key=api_key)
    movie_id = "non_existent_movie_id"
    movie = api.get_instance(Movie, movie_id)

    assert movie is None
