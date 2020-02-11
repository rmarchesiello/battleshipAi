
from typing import Dict, List, Tuple
import math, random, copy, abc
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError

class AIPlayer(Player):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["HumanPlayer"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["HumanPlayer"]) -> None:
        ai_names : List[str] = ["Bokun Wang", "Ikechi Iwuagwu", "Jinyue Song", "Grant Gilson", "Noah Ledesma", "Stephen Ott"]
        self.name = random.choice(ai_names)

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        pos_orientations : List[str] = ["horizontal", "vertical"]
        orientationcreated = random.choice(pos_orientations)
        return orientation.Orientation.from_string(orientationcreated)

    def get_start_coords(self, ship_: ship.Ship):
        row = random.randint(0, self.board.num_rows -1)
        col = random.randint(0, self.board.num_cols -1)
        return row, col

    @abc.abstractmethod
    def get_move(self) -> move.Move:
        ...

    def fire_at(self, row: int, col: int) -> None:
        opponent = self.opponents[0]
        if opponent.board.has_been_fired_at(row, col):
            raise FiringLocationError(' ')
        else:
            opponent.receive_fire_at(row, col)
            self.display_scanning_boards()
            self.display_firing_board()