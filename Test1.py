from Classes.Player import *
from Classes.Camera import *
from Classes.Planet import *


planet = Planet(500, 500, 700)
player = Player("Ship1", planet)
camera = Camera((27, 21, 89))

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

planet_img = pygame.image.load("./Images/TestPlanet.png")

while True:
    player.control(pygame.event.get())
    player.run()
    camera.cam_pos = player.ship.get_real_coords()
    camera.fill(screen)
    camera.drawing(screen, [player.ship.get_info_for_drawing(), {"x": planet.x, "y": planet.y,
                                                                 "width": planet.radius * 2,
                                                                 "height": planet.radius * 2,
                                                                 "image": planet_img,
                                                                 "rot": 0
                                                                 }], camera.cam_pos,
                   camera.zoom_value)
    camera.render()
