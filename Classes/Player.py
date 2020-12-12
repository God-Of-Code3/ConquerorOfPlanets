from Classes.Starship import *


class Player:
    def __init__(self, ship_type, planet):
        self.ship = Starship(270, 20, 154, 80, ship_type, planet)

    def control(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.ship.accelerate_y(1)
                if event.key == pygame.K_s:
                    self.ship.accelerate_y(-1)
                if event.key == pygame.K_a:
                    self.ship.accelerate_x(-1)
                if event.key == pygame.K_d:
                    self.ship.accelerate_x(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.ship.accelerate_y(0)
                if event.key == pygame.K_s:
                    self.ship.accelerate_y(0)
                if event.key == pygame.K_a:
                    self.ship.accelerate_x(0)
                if event.key == pygame.K_d:
                    self.ship.accelerate_x(0)

    def run(self):
        # print(self.ship.speed_x, self.ship.speed_y)
        self.ship.do()


