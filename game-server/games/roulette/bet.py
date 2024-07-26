from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List
from .roulette_game import PocketColor, RoulettePocket


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


@dataclass
class StraightUpBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.STRAIGHT_UP
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 35


@dataclass
class SplitBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.SPLIT
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 17


@dataclass
class StreetBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.STREET
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 11


@dataclass
class FiveNumberBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.FIVE_NUMBER_BET
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:

        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 11


@dataclass
class LineBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.LINE
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:

        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self):
        self.amount_won = self.bet_amount * 5


@dataclass
class DozenBet(RouletteBet):
    type: RouletteBetType = RouletteBetType.DOZEN
    bet_amount: float = None
    amount_won: float = None
    dozen: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:

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
    type: RouletteBetType = RouletteBetType.COLUMN
    bet_amount: float = None
    amount_won: float = None
    column: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:

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
    type: RouletteBetType = RouletteBetType.EIGHTEEN_NUMBER_BET
    amount_won: float = None
    bet: str = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:

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
    type: RouletteBetType = RouletteBetType.COLOR
    amount_won: float = None
    color: PocketColor = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.bet_amount = bet_amount
        self.pockets = pockets
        self.color = pockets[0].pocket_color

    def compute_winnings(self):
        self.amount_won = self.bet_amount


@dataclass
class OddOrEvenBet(RouletteBet):
    type: RouletteBetType
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.bet_amount = bet_amount
        self.pockets = pockets
        self.type = (
            RouletteBetType.EVEN
            if self.pockets[-1].pocket_number % 2 == 0
            else RouletteBetType.ODD
        )

    def compute_winnings(self):
        self.amount_won = self.bet_amount
