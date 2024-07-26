from random import Random

from games.roulette.bet import (
    ColorBet,
    ColumnBet,
    DozenBet,
    EighteenNumberBet,
    FiveNumberBet,
    LineBet,
    OddOrEvenBet,
    RouletteBet,
    RouletteBetType,
    SplitBet,
    StraightUpBet,
    StreetBet,
)
from games.roulette.roulette_game import PocketColor, RouletteGame

_roulette = RouletteGame()


def random_bet() -> RouletteBet:
    bet_type: RouletteBetType = Random().choice(list(RouletteBetType))
    if bet_type is RouletteBetType.STRAIGHT_UP:
        return _random_straight_up_bet()

    if bet_type is RouletteBetType.SPLIT:
        return _random_split_bet()

    if bet_type is RouletteBetType.STREET:
        return _random_street_bet()

    if bet_type is RouletteBetType.FIVE_NUMBER_BET:
        return _five_number_bet()

    if bet_type is RouletteBetType.LINE:
        return _random_line_bet()

    if bet_type is RouletteBetType.DOZEN:
        return _random_dozen_bet()

    if bet_type is RouletteBetType.COLUMN:
        return _random_column_bet()

    if bet_type is RouletteBetType.EIGHTEEN_NUMBER_BET:
        return _random_eighteen_number_bet()

    if bet_type is RouletteBetType.COLOR:
        return _random_color_bet()

    if bet_type is RouletteBetType.ODD:
        return _odd_or_even_bet(is_even=False)

    if bet_type is RouletteBetType.EVEN:
        return _odd_or_even_bet(is_even=True)


def _random_straight_up_bet() -> RouletteBet:
    row = Random().randint(1, 12)
    col = Random().randint(1, 3)
    random_pocket = _roulette.pocket_from_coord(row, col)

    return StraightUpBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[
            random_pocket,
        ],
    )


def _random_split_bet() -> RouletteBet:
    row = Random().randint(1, 12)
    col = Random().randint(1, 3)
    random_pocket = _roulette.pocket_from_coord(row, col)
    adj_rows = [i for i in [row - 1, row + 1] if i >= 1 and i <= 12]
    adj_cols = [i for i in [col - 1, col + 1] if i >= 1 and i <= 3]

    should_use_row = Random().random() < 0.5

    cell = Random().choice(adj_rows) if should_use_row else Random().choice(adj_cols)
    adj_row, adj_col = (cell, col) if should_use_row else (row, cell)

    adjacent_pocker = _roulette.pocket_from_coord(adj_row, adj_col)
    return SplitBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[random_pocket, adjacent_pocker],
    )


def _random_street_bet() -> RouletteBet:
    row = Random().randint(1, 12)
    return StreetBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[_roulette.pocket_from_coord(row, col) for col in range(1, 4)],
    )


def _five_number_bet() -> RouletteBet:
    return FiveNumberBet(
        bet_amount=Random().uniform(1, 100),
        pockets=_roulette.pockets_from_color(PocketColor.GREEN)
        + [_roulette.pocket_from_coord(1, col) for col in range(1, 4)],
    )


def _random_line_bet() -> RouletteBet:
    row = Random().randint(1, 11)
    return LineBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[_roulette.pocket_from_coord(row, col) for col in range(1, 4)]
        + [_roulette.pocket_from_coord(row + 1, col) for col in range(1, 4)],
    )


def _random_dozen_bet() -> RouletteBet:
    starting_number = Random().choice([1, 13, 25])
    return DozenBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[
            _roulette.pocket_from_pocket_number(pocket_number=pocket_number)
            for pocket_number in range(starting_number, starting_number + 12)
        ],
    )


def _random_column_bet() -> RouletteBet:
    col = Random().randint(1, 3)
    return ColumnBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[_roulette.pocket_from_coord(row, col) for row in range(1, 12)],
    )


def _random_eighteen_number_bet() -> RouletteBet:
    starting_number = Random().choice([1, 19])
    return EighteenNumberBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[
            _roulette.pocket_from_pocket_number(pocket_number=pocket_number)
            for pocket_number in range(starting_number, starting_number + 18)
        ],
    )


def _random_color_bet() -> RouletteBet:
    color = Random().choice(list(PocketColor))

    return ColorBet(
        bet_amount=Random().uniform(1, 100),
        pockets=_roulette.pockets_from_color(color),
    )


def _odd_or_even_bet(is_even: bool) -> RouletteBet:
    start = 0 if is_even else 1
    pockets = [
        _roulette.pocket_from_pocket_number(pocket_number=pocket_number)
        for pocket_number in range(start, 37, 2)
    ]

    if is_even:
        pockets = _roulette.pockets_from_color(PocketColor.GREEN) + pockets
    return OddOrEvenBet(
        bet_amount=Random().uniform(1, 100),
        pockets=pockets,
    )
