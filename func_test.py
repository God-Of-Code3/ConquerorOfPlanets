import math
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))


def get_rect_points(x, y, w, h, a):
    angle = math.atan(w / h) / math.pi * 180 + a
    angle2 = angle + (90 - angle) * 2
    angle3 = angle + 180
    angle4 = angle2 + 180
    hyp = math.hypot(w / 2, h / 2)
    points = [
        (x + math.cos(math.pi / 180 * angle) * hyp, y + math.sin(math.pi / 180 * angle) * hyp),
        (x + math.cos(math.pi / 180 * angle2) * hyp, y + math.sin(math.pi / 180 * angle2) * hyp),
        (x + math.cos(math.pi / 180 * angle3) * hyp, y + math.sin(math.pi / 180 * angle3) * hyp),
        (x + math.cos(math.pi / 180 * angle4) * hyp, y + math.sin(math.pi / 180 * angle4) * hyp),
    ]
    return points


def draw_point(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 1)

x, y = 250, 250
h, w = 100, 100

horizon_angle = 0

get_rect_points(x, y, w, h, 0)

while False:
    pygame.event.get()
    screen.fill((0, 0, 0))
    horizon_angle += 1
    for i in range(360):
        p_x = x + math.cos(math.pi / 180 * (i + 0)) * r1 + math.sin(math.pi / 180 * (i - horizon_angle)) * 10
        p_y = y + math.sin(math.pi / 180 * (i + 0)) * r1 + math.cos(math.pi / 180 * (i - horizon_angle)) * 10

    pygame.display.flip()