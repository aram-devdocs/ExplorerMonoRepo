from httplib2 import Http


def helper_function():
    return "Helper function result"


def fetch(url: str, params: dict = None) -> tuple:
    """
    Fetch data from a given URL with optional parameters.

    :param url: The URL to fetch data from.
    :param params: Optional parameters to include in the request.
    :return: A tuple containing the response and content.
    """
    if params is None:
        params = {}

    http = Http()
    response, content = http.request(url, "GET", body=params)
    return response, content
