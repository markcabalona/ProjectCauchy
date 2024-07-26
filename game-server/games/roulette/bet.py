from abc import ABC, abstractmethod
from enum import Enum
from typing import List
from .roulette_game import RoulettePocket


class RouletteBetType(Enum):
    STRAIGHT_UP: str = "STRAIGHT_UP"
    SPLIT: str = "SPLIT"
    STREET: str = "STREET"
    FIVE_NUMBER_BET: str = "FIVE_NUMBER_BET"
    LINE: str = "LINE"
    DOZEN: str = "DOZEN"
    COLUMN: str = "COLUMN"
    EIGHTEEN_NUMBER_BET: str = "EIGHTEEN_NUMBER_BET"
    COLOR: str = "COLOR"
    ODD: str = "ODD"
    EVEN: str = "EVEN"


class RouletteBet(ABC):
    type: RouletteBetType
    pockets: List[RoulettePocket]
    bet_amount: float
    amount_won: float = None

    @abstractmethod
    def compute_winnings() -> None:
        raise Exception("Unimplemented Error")

