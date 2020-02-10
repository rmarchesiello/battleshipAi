import unittest
from BattleShip.src.orientation import Orientation


class TestOrientation(unittest.TestCase):
    def test_create_horizontal(self):
        prefixes = ['horizontal', 'h', 'hor']
        for prefix in prefixes:
            with self.subTest(prefix=prefix):
                self.assertIs(Orientation.from_string(prefix), Orientation.HORIZONTAL)


if __name__ == '__main__':
    unittest.main()
