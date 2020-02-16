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
        self.is_sdai = False
        self.possible_moves = self.board.get_possible_moves()

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Random Ai {player_num}"

    def get_move(self) -> move.Move:
        selection = random.choice(self.possible_moves)
        self.possible_moves.remove(selection)
        raw_coords1 = str(selection)
        raw_coords2 = raw_coords1.replace('(', '')
        coords = raw_coords2.replace(')', '')
        firing_location = move.Move.from_str(self, coords)
        return firing_location
