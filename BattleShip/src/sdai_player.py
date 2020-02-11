from typing import Dict, List, Tuple
import math, random, copy, abc
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
from .aiplayer import AIPlayer

class HuntDestroyAIPlayer(AIPlayer):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List[Player]) -> None:
        super().__init__(player_num, config, other_players)

    def get_move(self) -> move.Move:
        pass