import unittest
import BattleShip.src.board as board
import BattleShip.src.game_config as config
import BattleShip.src.ship_placement as ship_placement
import BattleShip.src.orientation as orientation


class TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        classic_config = config.GameConfig('../configs/classic_game.txt')
        self.classic_board = board.Board(classic_config)
        for row, ship in enumerate(sorted(classic_config.available_ships.values())):
            self.classic_board.place_ship(ship_placement.ShipPlacement(
                ship,
                orientation.Orientation.HORIZONTAL,
                row, 0))

    def test_classic_board_visible_display(self):
        correct_display = '  0 1 2 3 4 5 6 7 8 9\n' \
                          '0 B B B B * * * * * *\n' \
                          '1 C C C C C * * * * *\n' \
                          '2 D D D * * * * * * *\n' \
                          '3 P P * * * * * * * *\n' \
                          '4 S S S * * * * * * *\n' \
                          '5 * * * * * * * * * *\n' \
                          '6 * * * * * * * * * *\n' \
                          '7 * * * * * * * * * *\n' \
                          '8 * * * * * * * * * *\n' \
                          '9 * * * * * * * * * *\n'

        self.assertEqual(self.classic_board.get_display(hidden=False), correct_display)


def test_classic_board_hidden_display(self):
    correct_display = '  0 1 2 3 4 5 6 7 8 9\n' \
                      '0 * * * * * * * * * *\n' \
                      '1 * * * * * * * * * *\n' \
                      '2 * * * * * * * * * *\n' \
                      '3 * * * * * * * * * *\n' \
                      '4 * * * * * * * * * *\n' \
                      '5 * * * * * * * * * *\n' \
                      '6 * * * * * * * * * *\n' \
                      '7 * * * * * * * * * *\n' \
                      '8* * * * * * * * * *\n' \
                      '9 * * * * * * * * * *\n'

    self.assertEqual(self.classic_board.get_display(hidden=True), correct_display)


if __name__ == '__main__':
    unittest.main()
