from Classes.Starship import *
from Classes.Planet import *


class Player:
    def __init__(self, ship_type, planet):
        self.ship = Starship(270, 20, 100, 20, ship_type, planet)

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


planet = Planet(500, 500, 110)
player = Player("Ship1", planet)

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
while True:
    #screen.fill((0, 0, 0))

    player.control(pygame.event.get())
    player.run()
    pygame.draw.polygon(screen, (255, 255, 255), player.ship.get_my_polygon(), 4)
    pygame.draw.circle(screen, (255, 255, 255), (planet.x, planet.y), planet.radius, 2)

    pygame.display.flip()
