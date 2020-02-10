from . import player
from .firing_location_error import FiringLocationError


class Move(object):
    def __init__(self, maker: "player.Player", row, col) -> None:
        super().__init__()
        self.maker = maker
        self.row = row
        self.col = col
        self._ends_turn = False

    @classmethod
    def from_str(cls, maker: "player.Player", str_rep: str) -> "Move":
        try:
            row, col = str_rep.split(',')
        except ValueError:
            raise ValueError(f'{str_rep} is not a valid location.\n'
                             f'Enter the firing location in the form row, column')
        try:
            row = int(row)
        except ValueError:
            raise ValueError(f'Row should be an integer. {row} is NOT an integer.')
        try:
            col = int(col)
        except ValueError:
            raise ValueError(f'Column should be an integer. {col} is NOT an integer.')
        return cls(maker, row, col)

    def make(self) -> None:
        try:
            self.maker.fire_at(self.row, self.col)
        except FiringLocationError as e:
            print(e)
        else:
            self._ends_turn = True

    def __str__(self) -> str:
        return f'{self.row}, {self.col}'

    def __repr__(self) -> str:
        return str(self)

    def ends_turn(self) -> bool:
        return self._ends_turn
