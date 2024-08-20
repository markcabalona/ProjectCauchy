import json
from typing import List
from requests import get, Response


def extract(base_url: str, games_count: int = 1) -> json:
    url = f"http://{base_url}:8000/roulette"

    result: List = []
    for _ in range(games_count):
        response: Response = get(url)
        if response.ok:
            result.append(response.json())

    return result
