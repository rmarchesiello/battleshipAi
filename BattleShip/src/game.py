import itertools, sys, random
from . import game_config, human_player, randomai_player, cheatingai_player, sdai_player, player

class Game(object):
    def __init__(self, game_config_file: str, seed: int, num_players: int = 2) -> None:
        super().__init__()
        self.game_config = game_config.GameConfig(game_config_file, seed)
        random.seed(seed)
        self.players = []
        self.player_turn = 0
        self.player_types = ['Human', 'CheatingAi', 'SearchDestroyAi', 'RandomAi']
        self.setup_players(num_players)

    def setup_players(self, num_players: int) -> None:
        for i in range(1,3):
            raw_selection = input(f"Enter one of {self.player_types} for Player {i}'s type: ")
            if raw_selection[0].lower() == 'h':
                self.players.append(human_player.HumanPlayer(i, self.game_config, self.players))
            elif raw_selection[0].lower() == 'c':
                self.players.append(cheatingai_player.CheatingAIPlayer(i, self.game_config, self.players))
            elif raw_selection[0].lower() == 's':
                self.players.append(sdai_player.HuntDestroyAIPlayer(i, self.game_config, self.players))
            elif raw_selection[0].lower() == 'r':
                self.players.append(randomai_player.RandomAIPlayer(i, self.game_config, self.players))

    def play(self) -> None:
        active_player = self.players[0]
        for active_player in itertools.cycle(self.players):
            self.do_current_players_turn(active_player)
            if self.game_is_over():
                break
        print(f'{active_player} won the game!')

    def do_current_players_turn(self, cur_player: player.Player) -> None:
        self.display_gamestate(cur_player)
        while True:
            move = cur_player.get_move()
            move.make()
            if move.ends_turn():
                break

    @property
    def num_players(self) -> int:
        return len(self.players)

    def get_active_player(self) -> human_player.HumanPlayer:
        return self.players[self.player_turn]

    def game_is_over(self) -> bool:
        return any(player_.all_ships_sunk() for player_ in self.players)

    def display_gamestate(self, cur_player: human_player.HumanPlayer) -> None:
        cur_player.display_scanning_boards()
        cur_player.display_firing_board()