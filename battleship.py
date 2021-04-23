from ship import *


class Battleship:
    def __init__(self, player1, player2):
        self.grid = []
        self.player1 = player1
        self.player2 = player2

    def create_grid(self, rows, cols):
        self.grid = [[0 for x in range(rows)] for y in range(cols)]

        for row in self.grid:
            print(row)

    def create_fleet(self, player):
        destroyer = Destroyer()
        submarine = Submarine()
        battleship = Battleship()
        carrier = Carrier()

        player.ship_fleet.append(destroyer)
        player.ship_fleet.append(submarine)
        player.ship_fleet.append(battleship)
        player.ship_fleet.append(carrier)

    def modify_grid_element(self):
        pass
