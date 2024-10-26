import os


BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:5000")
API_PARAM = os.getenv("API_PATH", "/api")
API_PATH = f"{BASE_URL}{API_PARAM}"
