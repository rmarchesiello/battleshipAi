from typing import Dict, List
import math, copy, abc, random
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
from .aiplayer import AIPlayer

class RandomAIPlayer(AIPlayer):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.is_sdai = True

    def get_move(self) -> move.Move:
        move_index = random.randint(0, len(self.possible_moves))
        raw_coords1 = str(self.possible_moves.pop(move_index))
        raw_coords2 = raw_coords1.replace('(', '')
        coords = raw_coords2.replace(')', '')
        firing_location = move.Move.from_str(self, coords)
        return firing_location
