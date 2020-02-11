from typing import Dict, List
import copy
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
import abc

class CheatingAIPlayer(Player):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["HumanPlayer"]) -> None:
        super().__init__(player_num, config, other_players)

    def init_name(self, player_num: int, other_players: List["HumanPlayer"]) -> None:
        pass

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        pass

    def get_start_coords(self, ship_: ship.Ship):
        pass

    def get_move(self) -> move.Move:
        pass

    def fire_at(self, row: int, col: int) -> None:
        pass

