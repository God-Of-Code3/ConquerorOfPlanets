class Enemy:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def get_information(self):
        info = [ship.get_info_for_drawing() for ship in self.ships]
        return info

