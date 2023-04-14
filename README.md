# The One API SDK

A Python SDK for The One API, which provides access to information about The Lord of the Rings and The Hobbit movies.

## Installation

To install the SDK, run:
```
pip install 'one-api-sid-sdk @ git+https://github.com/sid9102/sid-one-sdk@0.1.0'

```
This is installed directly from the 0.1.0 tag on the GitHub repository, allowing us 
to avoid dumping a useless SDK on PyPI!

## Usage

First, import the necessary classes:
```python
from one_api_sdk.client import OneApiClient
from one_api_sdk.models.movie import Movie
from one_api_sdk.filter import Filter
```

Create an instance of the `OneApiClient` with your API key:
```python
api_key = "your-api-key"
client = OneApiClient(api_key)
```

To get all movies:
```python
movies = client.get_all(Movie)
```

To get a specific movie:
```python
movie_id = "5cd95395de30eff6ebcce7e8"
movie = client.get_instance(Movie, movie_id)
```

To get all quotes for a specific movie:
```python
quotes = client.get_all(Quote, parent_model=Movie, parent_id=movie_id)
```

## Advanced Queries

### Filtering

To filter results, use the `Filter` class. For example, to get all movies with a runtime greater than 180 minutes:

```python
runtime_filter = Filter("runtimeInMinutes", FilterOperation.GT, 180)
movies = client.get_all(Movie, filters=[runtime_filter])
```

See the [Filter class](one_api_sid_sdk/filter.py) for more information on available operations.

### Sorting

To sort results, pass the `sort` parameter with the field name and set the `ascending` parameter to `True` (default) or `False`. For example, to get all movies sorted by runtime in descending order:

```python
movies = client.get_all(Movie, sort="runtimeInMinutes", ascending=False)
```

### Pagination

To paginate results, use the `limit`, `page`, and `offset` parameters. The `limit` parameter sets the maximum number of results per page, while the `page` parameter determines the current page. The `offset` parameter sets the number of results to skip before starting to return results. For example, to get the second page of movies with a limit of 5 movies per page:

```python
movies = client.get_all(Movie, limit=5, page=2)
```

To get movies starting from the 11th result:

```python
movies = client.get_all(Movie, limit=5, offset=10)
```

Please note that not all fields support filtering and sorting. Refer to [The One API documentation](https://the-one-api.dev/documentation#5) for details on which fields can be used for these operations.
## Testing

Add a file called `API_KEY` to the root of the project with your API key from [your account page](https://the-one-api.dev/account). This is optional; if the file is not provided, any tests that require it will be skipped.

Run the tests with `pytest`:
```
pytest
```

## Design

For information on the SDK design, see [design.md](design.md) file in the root directory.