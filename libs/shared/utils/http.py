from httplib2 import Http
from libs.shared.consts import API_PATH


def get(endpoint: str, params: dict = None) -> tuple:
    """
    Fetch data from a given URL with optional parameters.

    :param endpoint: The API endpoint to fetch data from. EX: /users
    :param params: Optional parameters to include in the request.
    :return: A tuple containing the response and content.
    """
    if params is None:
        params = {}

    http = Http()
    response, content = http.request(f"{API_PATH}{endpoint}", "GET", body=params)
    return response, content


def post(endpoint: str, data: dict) -> tuple:
    """
    Send data to a given URL using POST method.

    :param endpoint: The API endpoint to send data to. EX: /users
    :param data: The data to send in the request body.
    :return: A tuple containing the response and content.
    """
    http = Http()
    response, content = http.request(f"{API_PATH}{endpoint}", "POST", body=data)
    return response, content


def put(endpoint: str, data: dict) -> tuple:
    """
    Update data at a given URL using PUT method.

    :param endpoint: The API endpoint to update data at. EX: /users
    :param data: The data to update in the request body.
    :return: A tuple containing the response and content.
    """
    http = Http()
    response, content = http.request(f"{API_PATH}{endpoint}", "PUT", body=data)
    return response, content


def delete(endpoint: str) -> tuple:
    """
    Delete data at a given URL using DELETE method.

    :param endpoint: The API endpoint to delete data from. EX: /users
    :return: A tuple containing the response and content.
    """
    http = Http()
    response, content = http.request(f"{API_PATH}{endpoint}", "DELETE")
    return response, content
