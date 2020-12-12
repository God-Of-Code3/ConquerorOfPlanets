import pygame
from Classes.Math import *
pygame.init()
screen = pygame.display.set_mode((500, 500))

angle = 0
while True:
    pygame.event.get()
    screen.fill((0, 0, 0))
    angle += 0.1
    angle = angle % 360
    pygame.draw.line(screen, (255, 255, 255), (0, 250), (500, 250), 2)
    pygame.draw.line(screen, (255, 255, 255), (250, 0), (250, 500), 2)
    img = pygame.image.load("./Images/Starship1.png")
    img = pygame.transform.scale(img, (154, 80))
    img = pygame.transform.rotate(img, angle)
    polygon = rotate_polygon(0, 0, [[-77, -40], [77, -40], [77, 40], [-77, 40]], angle)
    min_x = min(polygon, key=lambda x: x[0])
    max_x = max(polygon, key=lambda x: x[0])
    min_y = min(polygon, key=lambda x: x[1])
    max_y = max(polygon, key=lambda x: x[1])
    width = max_x[0] - min_x[0]
    height = max_y[1] - min_y[1]
    screen.blit(img, (250 - width / 2, 250 - height / 2))
    pygame.display.flip()