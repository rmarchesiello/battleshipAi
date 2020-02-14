
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
        self.temp_ori = ''

    #def init_name(self, player_num: int, other_players: List["HumanPlayer"]) -> None:
    #    ai_names : List[str] = ["Bokun Wang", "Ikechi Iwuagwu", "Jinyue Song", "Grant Gilson", "Noah Ledesma", "Stephen Ott"]
    #    self.name = random.choice(ai_names)

    def get_orientation(self, ship_: ship.Ship) -> orientation.Orientation:
        pos_orientations : List[str] = ["horizontal", "vertical"]
        orientationcreated = random.choice(pos_orientations)
        self.temp_ori = orientationcreated
        
        return orientation.Orientation.from_string(orientationcreated)

    def get_start_coords(self, ship_: ship.Ship): #this might be where the problem is, find a way to check board bounds here
        if self.temp_ori == 'vertical':
            row = random.randint(0, self.board.num_rows - ship_.length)
            col = random.randint(0, self.board.num_cols - 1)
            return row, col
        elif self.temp_ori == 'horizontal':
            row = random.randint(0, self.board.num_rows - 1)
            col = random.randint(0, self.board.num_cols - ship_.length)
            return row, col

    def place_ship(self, ship_: ship.Ship) -> None:
        while True:
            placement = self.get_ship_placement(ship_)
            try:
                self.board.place_ship(placement)
                self.ship_placements = self.board.save_placements(placement)
                self.ship_placements.sort()
            except ValueError as e:
                continue
            else:
                return

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