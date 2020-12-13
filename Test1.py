from Classes.Player import *
from Classes.Camera import *
from Classes.Planet import *
from Classes.Enemy import *


planet = Planet(500, 500, 1000)
player = Player("Ship1", planet)
enemy = Enemy()

for i in range(0, 360, 20):
    enemy.add_ship(Starship(i, i, 38, 20, "Ship1", planet))
camera = Camera((27, 21, 89))

pygame.init()
screen = pygame.display.set_mode((1500, 1000))

planet_img = pygame.image.load("./Images/TestPlanet.png")

moving_event = pygame.USEREVENT + 1
pygame.time.set_timer(moving_event, 10)
while True:
    events = pygame.event.get()
    player.control(events)
    #camera.zoom_value = (planet.radius + 20) / (player.ship.y + planet.radius)
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:  # Изменение зума
            if event.button == 4:
                camera.zoom(ZOOM_SENSITIVITY)
            elif event.button == 5:
                camera.zoom(1 / ZOOM_SENSITIVITY)
        if event.type == moving_event:
            player.run(enemy.ships)
    #camera.zoom_value = (20 + planet.radius) / (player.ship.y + planet.radius)
    camera.cam_pos = player.ship.get_real_coords()
    camera.fill(screen)
    camera.drawing(screen, [player.ship.get_info_for_drawing(), *enemy.get_information()], camera.cam_pos,
                   camera.zoom_value)
    camera.drawing_planet(screen, planet, camera.cam_pos,
                   camera.zoom_value)
    #print(rotate_polygon(*player.ship.get_real_coords(), player.ship.get_my_polygon(),
    #                                              player.ship.x))
    #camera.drawing_polygon(screen, player.ship.get_my_polygon(),
    #                       camera.cam_pos, camera.zoom_value)
    #for enem in enemy.ships:
        #camera.drawing_polygon(screen, enem.get_my_polygon(),
        #                       camera.cam_pos, camera.zoom_value)
    camera.render()
