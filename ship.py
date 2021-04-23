class Ship:
    def __init__(self, name):
        self.is_sunk = False
        self.is_placed = False
        self.name = name


class Destroyer(Ship):
    def __init__(self):
        super(Destroyer, self).__init__("Destroyer")
        self.hit_points = 2


class Submarine(Ship):
    def __init__(self):
        super(Submarine, self).__init__("Submarine")
        self.hit_points = 3


class Battleship(Ship):
    def __init__(self):
        super(Battleship, self).__init__("Battleship")
        self.hit_points = 4


class Carrier(Ship):
    def __init__(self):
        super(Ship, self).__init__("Carrier")
        self.hit_points = 5