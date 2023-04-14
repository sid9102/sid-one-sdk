import os

import pytest


def requires_api_key(func):
    """
    A custom pytest decorator that skips the decorated test function if the
    "API_KEY" file is not found in the project root directory.

    Usage:

    @requires_api_key
    def test_that_requires_api_key():
        # Your test code here
    """
    API_KEY_FOUND = os.path.exists("API_KEY")
    return pytest.mark.skipif(
        not API_KEY_FOUND,
        reason="API_KEY file not found"
    )(func)
