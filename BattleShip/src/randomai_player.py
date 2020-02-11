from typing import Dict, List
import math, copy, abc, random
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
from .aiplayer import AIPlayer

class RandomAIPlayer(AIPlayer):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["HumanPlayer"]) -> None:
        super().__init__(player_num, config, other_players)

    def get_move(self) -> move.Move:
        rand_move_row = random.randint(0, self.board.num_rows -1)
        rand_move_col = random.randint(0, self.board.num_cols -1)
        coords = f"{rand_move_row}, {rand_move_col}"
        firing_location = move.Move.from_str(self, coords)
        return firing_location
