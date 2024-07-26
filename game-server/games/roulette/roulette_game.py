from enum import Enum
from random import Random
from typing import List


class PocketColor(Enum):
    RED: str = "RED"
    BLACK: str = "BLACK"
    GREEN: str = "GREEN"


class RoulettePocket:
    """
    Represents a pocket in a Roulette
    - [pocket_color]: The color of the winning pocket
    - [pocket_number]: The number of the winning pocket, -1 being the double-zero (00) and 0 being zero(0)
    """

    pocket_color: PocketColor
    pocket_number: int

    def __init__(self, pocket_number) -> None:
        self.pocket_number = pocket_number
        self.pocket_color = self._get_pocket_color()

    def _get_pocket_color(self) -> PocketColor:
        if self.pocket_number <= 0:
            return PocketColor.GREEN
        is_even = self.pocket_number % 2 == 0
        if self.pocket_number <= 10:
            return PocketColor.BLACK if is_even else PocketColor.RED
        if self.pocket_number <= 18:
            return PocketColor.RED if is_even else PocketColor.BLACK
        if self.pocket_number <= 28:
            return PocketColor.BLACK if is_even else PocketColor.RED

        return PocketColor.RED if is_even else PocketColor.BLACK

    def __eq__(self, other):
        if not isinstance(other, RoulettePocket):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.pocket_number == other.pocket_number
            and self.pocket_color == other.pocket_color
        )


class RouletteGame:
    _instance = None
    pockets = List[RoulettePocket]

    def __new__(self):
        if self._instance is None:
            self._instance = super(RouletteGame, self).__new__(self)
            self.pockets = [RoulettePocket(pocket_number=i) for i in range(-1, 37)]
        return self._instance

    def spin(self) -> RoulettePocket:
        row = Random().randint(1, 12)
        col = Random().randint(1, 3)
        return self.pocket_from_coord(row, col)

    def pocket_from_coord(self, row: int, col: int) -> RoulettePocket:
        pocket_number = col + ((row - 1) * 3)
        for pocket in self.pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pocket_from_pocket_number(self, pocket_number: int) -> RoulettePocket:
        for pocket in self.pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pockets_from_color(self, color: PocketColor) -> List[RoulettePocket]:
        return [pocket for pocket in self.pockets if pocket.pocket_color == color]
