from httplib2 import Http, HttpLib2Error
from libs.shared.consts import API_PATH
import json


class HttpClient:
    def __init__(self):
        self.http = Http()
        self.headers = {"Content-Type": "application/json"}

    def get(self, endpoint: str, params: dict = None) -> tuple:
        if params is None:
            params = {}
        try:
            response, content = self.http.request(
                f"{API_PATH}{endpoint}",
                "GET",
                headers=self.headers,
                body=json.dumps(params),
            )
            return response, content
        except HttpLib2Error as e:
            return None, f"An error occurred: {e}"

    def post(self, endpoint: str, data: dict) -> tuple:
        try:
            response, content = self.http.request(
                f"{API_PATH}{endpoint}",
                "POST",
                headers=self.headers,
                body=json.dumps(data),
            )
            return response, content
        except HttpLib2Error as e:
            return None, f"An error occurred: {e}"

    def put(self, endpoint: str, data: dict) -> tuple:
        try:
            response, content = self.http.request(
                f"{API_PATH}{endpoint}",
                "PUT",
                headers=self.headers,
                body=json.dumps(data),
            )
            return response, content
        except HttpLib2Error as e:
            return None, f"An error occurred: {e}"

    def delete(self, endpoint: str) -> tuple:
        try:
            response, content = self.http.request(
                f"{API_PATH}{endpoint}", "DELETE", headers=self.headers
            )
            return response, content
        except HttpLib2Error as e:
            return None, f"An error occurred: {e}"
