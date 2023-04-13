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
