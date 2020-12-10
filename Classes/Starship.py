from Classes.Constants import *


class Starship:
    def __init__(self, x, y, width, height, ship_type, health=1000, image="Ship1.png"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        if ship_type != 0:
            self.type = ship_type
            ship = STARSHIPS[ship_type]
            self.health = ship["health"]
            self.image = ship["image"]
        else:
            self.type = "Пользовательский"
            self.health = health
            self.image = image