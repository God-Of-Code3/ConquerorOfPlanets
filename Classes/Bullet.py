from Classes.Math import *


class Bullet:
    def __init__(self, x, y, direction, speed):
        self.x = x
        self.y = y
        self.speed_x = math.cos(direction * math.pi / 180) * speed
        self.speed_y = math.cos(direction * math.pi / 180) * speed
        self.direction = direction
        self.image = "../Images/"

    def move(self, polygons):
        self.x += self.speed_x
        self.y += self.speed_y
        for polygon in polygons:
            if check_point_intersection(polygon, (self.x, self.y)):
                self.x -= self.speed_x
                self.y -= self.speed_y
                break

