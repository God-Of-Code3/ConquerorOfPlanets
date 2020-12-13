import pygame
import random


class Planet:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))
