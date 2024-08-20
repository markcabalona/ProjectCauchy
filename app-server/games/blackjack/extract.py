import json
from typing import Optional
from requests import get, Response


def extract(
    base_url: str,
    players: Optional[int] = None,
    games: Optional[int] = None,
) -> json:
    url = f"http://{base_url}:8000/blackjack"

    response: Response = get(
        url,
        params={
            "players": players,
            "games": games,
        },
    )

    if response.ok:
        return response.json()
    else:
        raise Exception(response.json())
