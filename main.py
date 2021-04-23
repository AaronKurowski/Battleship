from game import Game
from battleship import Battleship

if __name__ == '__main__':

    # game = Game()
    # game.play_battleship()
    #
    #
    # rows, cols = (3, 3)
    #
    # grid = [[0 for x in range(rows)] for y in range(cols)]
    #
    # grid[0][0] = 1
    # for row in grid:
    #     print(row)

    battleship = Battleship('1', '2')
    battleship.create_grid(20, 20)
