from dataclasses import asdict

from fastapi import FastAPI
from games.bigwheel import simulate_bigwheel
from games.poker import simulate_poker
from games.roulette import simulate_roulette

app = FastAPI()

@app.get("/poker")
def get_poker():
    return asdict(simulate_poker())

@app.get("/bigwheel")
def get_bigwheel():
    return asdict(simulate_bigwheel())


@app.get("/roulette")
def get_roulette():
    return asdict(simulate_roulette())
