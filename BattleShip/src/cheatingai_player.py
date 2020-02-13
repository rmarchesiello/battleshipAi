from typing import Dict, List, Tuple
import math, random, copy, abc
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
from .aiplayer import AIPlayer

class CheatingAIPlayer(AIPlayer):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["HumanPlayer"]) -> None:
        super().__init__(player_num, config, other_players)
        self.is_sdai = False

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Cheating Ai {player_num}"

    def get_move(self) -> move.Move:
        move_index = random.randint(0, len(self.opponents[0].board.ship_coords)-1)
        raw_coords1 = str(self.opponents[0].board.ship_coords.pop(0))
        raw_coords2 = raw_coords1.replace('(', '')
        coords = raw_coords2.replace(')', '')
        print(coords)
        firing_location = move.Move.from_str(self, coords)
        return firing_location

