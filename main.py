import sys
from BattleShip.src import game

if __name__ == '__main__':
    seed = 10
    if len(sys.argv) >= 3:
        print("seed provided")
        with open(sys.argv[2]) as seedfile:
            seed = seedfile.read()
    if len(sys.argv) <= 1:
        print('Not enough arguments given.')
    else:
        game_of_battle_ship = game.Game(sys.argv[1], seed)
        game_of_battle_ship.play()