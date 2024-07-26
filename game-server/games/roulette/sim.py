from dataclasses import dataclass

from typing import Dict, List
from copy import deepcopy

from games.roulette.bet import RouletteBet
from games.roulette.random_bet import random_bet


from .roulette_game import RouletteGame, RoulettePocket


@dataclass
class RouletteResult:
    winning_pocket: RoulettePocket
    winning_bets: Dict
    bets: List


def simulate_roulette() -> RouletteResult:
    winning_pocket = RouletteGame().spin()

    bets = [random_bet() for _ in range(100)]

    winning_bets = list(
        map(
            _compute_winnings,
            [bet for bet in deepcopy(bets) if winning_pocket in bet.pockets],
        )
    )

    return RouletteResult(
        winning_pocket=winning_pocket,
        winning_bets=winning_bets,
        bets=bets,
    )


def _compute_winnings(bet: RouletteBet) -> RouletteBet:
    bet.compute_winnings()
    return bet
