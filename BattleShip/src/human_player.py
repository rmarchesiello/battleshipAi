from typing import Dict, List
import copy
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
import abc

class HumanPlayer(Player):
    opponents: List["HumanPlayer"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["HumanPlayer"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["HumanPlayer"]) -> None:
        while True:
            self.name = input(f'HumanPlayer {player_num} please enter your name: ').strip()
            if self in other_players:
                print(f'Someone is already using {self.name} for their name.\n'
                      f'Please choose another name.')
            else:
                break

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        orientation_ = input(
            f'{self.name} enter horizontal or vertical for the orientation of {ship_.name} '
            f'which is {ship_.length} long: ')
        return orientation.Orientation.from_string(orientation_)

    def get_start_coords(self, ship_: ship.Ship):

        coords = input(f'{self.name}, enter the starting position for your {ship_.name} ship '
                       f',which is {ship_.length} long, in the form row, column: ')
        try:
            row, col = coords.split(',')
        except ValueError:
            raise ValueError(f'{coords} is not in the form x,y')

        try:
            row = int(row)
        except ValueError:
            raise ValueError(f'{row} is not a valid value for row.\n'
                             f'It should be an integer between 0 and {self.board.num_rows - 1}')

        try:
            col = int(col)
        except ValueError:
            raise ValueError(f'{col} is not a valid value for column.\n'
                             f'It should be an integer between 0 and {self.board.num_cols - 1}')

        return row, col

    def get_move(self) -> move.Move:
        while True:
            coords = input(f'{self.name}, enter the location you want to fire at in the form row, column: ')
            try:
                firing_location = move.Move.from_str(self, coords)
            except ValueError as e:
                print(e)
                continue
            return firing_location

    def fire_at(self, row: int, col: int) -> None:
        opponent = self.opponents[0]
        if not opponent.board.coords_in_bounds(row, col):
            raise FiringLocationError(f'{row}, {col} '
                                      f'is not in bounds of our '
                                      f'{opponent.board.num_rows} X {opponent.board.num_cols} board.')
        elif opponent.board.has_been_fired_at(row, col):
            raise FiringLocationError(f'You have already fired at {row}, {col}.')
        else:
            opponent.receive_fire_at(row, col)
            self.display_scanning_boards()
            self.display_firing_board()