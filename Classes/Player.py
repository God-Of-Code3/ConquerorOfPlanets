from Classes.Starship import *


class Player:
    def __init__(self, ship_type, planet):
        self.ship = Starship(270, 38, 38, 20, ship_type, planet)

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

    def run(self, enemys):
        # print(self.ship.speed_x, self.ship.speed_y)
        self.ship.do()
        for enemy in enemys:
            if check_intersection(self.ship.get_my_polygon(),
                                  enemy.get_my_polygon()):
                self.ship.speed_x = -self.ship.speed_x
                self.ship.speed_y = -self.ship.speed_y
                self.ship.move()
                self.ship.speed_x = -self.ship.speed_x
                self.ship.speed_y = -self.ship.speed_y

