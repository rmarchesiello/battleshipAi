from typing import Dict, List, Tuple
import math, random, copy, abc
from . import game_config, board, ship, orientation, ship_placement, move
from .player import Player
from .firing_location_error import FiringLocationError
from .aiplayer import AIPlayer

class HuntDestroyAIPlayer(AIPlayer):
    opponents: List["Player"]
    ships: Dict[str, ship.Ship]

    def __init__(self, player_num: int, config: game_config.GameConfig, other_players: List["Player"]) -> None:
        super().__init__(player_num, config, other_players)
        self.destroy_flag = False
        self.destroy_mode_moves = []
        self.possible_moves = self.board.get_possible_moves()
        self.is_sdai = True

    def init_name(self, player_num: int, other_players: List["Player"]) -> None:
        self.name = f"Search Destroy AI {player_num}"

    def get_move(self) -> move.Move:
        if self.destroy_flag is True and len(self.destroy_mode_moves) > 0:
            return self.get_destroy_move()
        else:
            self.destroy_flag = False
            return self.get_search_move()

    def get_search_move(self) -> move.Move:
        selection = random.choice(self.possible_moves)
        self.possible_moves.remove(selection)
        raw_coords1 = str(selection)
        raw_coords2 = raw_coords1.replace('(', '')
        coords = raw_coords2.replace(')', '')
        firing_location = move.Move.from_str(self, coords)
        return firing_location

    def get_destroy_move(self) -> move.Move:
        selection = random.choice(self.destroy_mode_moves)
        self.destroy_mode_moves.remove(selection)
        if selection in self.possible_moves:
            self.possible_moves.remove(selection)
        raw_coords1 = str(selection)
        raw_coords2 = raw_coords1.replace('(', '')
        coords = raw_coords2.replace(')', '')
        firing_location = move.Move.from_str(self, coords)
        return firing_location