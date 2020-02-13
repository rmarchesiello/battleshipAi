import sys
from BattleShip.src import game

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        seed = int(sys.argv[2])
    if len(sys.argv) <= 1:
        print('Not enough arguments given.')
    else:
        game_of_battle_ship = game.Game(sys.argv[1], seed)
        game_of_battle_ship.play()