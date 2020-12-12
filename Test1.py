from Classes.Player import *
from Classes.Camera import *
from Classes.Planet import *


planet = Planet(500, 500, 2000)
player = Player("Ship1", planet)
camera = Camera((27, 21, 89))

pygame.init()
screen = pygame.display.set_mode((1500, 1000))

planet_img = pygame.image.load("./Images/TestPlanet.png")

moving_event = pygame.USEREVENT + 1
pygame.time.set_timer(moving_event, 10)
while True:
    events = pygame.event.get()
    player.control(events)
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:  # Изменение зума
            if event.button == 4:
                camera.zoom(ZOOM_SENSITIVITY)
            elif event.button == 5:
                camera.zoom(1 / ZOOM_SENSITIVITY)
        if event.type == moving_event:
            player.run()
    #camera.zoom_value = (20 + planet.radius) / (player.ship.y + planet.radius)
    camera.cam_pos = player.ship.get_real_coords()
    camera.fill(screen)
    camera.drawing(screen, [player.ship.get_info_for_drawing(), {"x": planet.x, "y": planet.y,
                                                                 "width": planet.radius * 2,
                                                                 "height": planet.radius * 2,
                                                                 "real_width": planet.radius * 2,
                                                                 "real_height": planet.radius * 2,
                                                                 "image": planet_img,
                                                                 "rot": 0
                                                                 }], camera.cam_pos,
                   camera.zoom_value)
    camera.render()
