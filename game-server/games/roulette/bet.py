from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from random import Random
import string
from typing import List
from .roulette_game import PocketColor, RoulettePocket


def _generate_id() -> str:
    return "RBID-" + "".join(
        Random().choices(
            string.ascii_uppercase + string.digits,
            k=6,
        )
    )


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
    id: str = None
    type: RouletteBetType
    pockets: List[RoulettePocket]
    bet_amount: float
    amount_won: float = None

    @abstractmethod
    def compute_winnings() -> None:
        raise Exception("Unimplemented Error")


@dataclass
class StraightUpBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.STRAIGHT_UP
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 35


@dataclass
class SplitBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.SPLIT
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 17


@dataclass
class StreetBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.STREET
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 11


@dataclass
class FiveNumberBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.FIVE_NUMBER_BET
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 11


@dataclass
class LineBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.LINE
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 5


@dataclass
class DozenBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.DOZEN
    bet_amount: float = None
    amount_won: float = None
    dozen: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets
        if pockets[0].pocket_number == 1:
            self.dozen = "1st Dozen"
        elif pockets[0].pocket_number == 13:
            self.dozen = "2nd Dozen"
        else:
            self.dozen = "3rd Dozen"

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 2


@dataclass
class ColumnBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.COLUMN
    bet_amount: float = None
    amount_won: float = None
    column: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets
        if pockets[0].pocket_number == 1:
            self.column = "1st Column"
        elif pockets[0].pocket_number == 2:
            self.column = "2nd Column"
        else:
            self.column = "3rd Column"

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 2


@dataclass
class EighteenNumberBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.EIGHTEEN_NUMBER_BET
    bet_amount: float = None
    amount_won: float = None
    bet: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets
        if pockets[0].pocket_number == 1:
            self.bet = "1st Eighteen"
        else:
            self.bet = "2nd Eighteen"

    def compute_winnings(self):
        self.amount_won = self.bet_amount


@dataclass
class ColorBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.COLOR
    bet_amount: float = None
    amount_won: float = None
    color: PocketColor = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets
        self.color = pockets[0].pocket_color

    def compute_winnings(self):
        self.amount_won = self.bet_amount


@dataclass
class OddOrEvenBet(RouletteBet):
    id: str = None
    type: RouletteBetType = None
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets
        self.type = (
            RouletteBetType.EVEN
            if self.pockets[-1].pocket_number % 2 == 0
            else RouletteBetType.ODD
        )

    def compute_winnings(self):
        self.amount_won = self.bet_amount
