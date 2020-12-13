import math
from shapely.geometry import Polygon


def to_point(x1, y1, x2, y2):
    if y1 == y2:
        direction = 0 if x2 > x1 else 180
    elif x1 == x2:
        direction = 90 if y2 > y1 else 270
    else:
        direction = -math.atan((x2 - x1) / (y2 - y1)) / math.pi * 180 + 90
        if y2 < y1:
            direction += 180
    if direction < 0:
        direction = 360 + direction
    return direction


def rotate_polygon(x, y, points, a):
    new_points = []
    for point in points:
        dist = math.hypot(point[0], point[1])
        direction = to_point(0, 0, point[0], point[1]) + a
        new_x = x + math.cos(math.pi / 180 * direction) * dist
        new_y = y + math.sin(math.pi / 180 * direction) * dist
        new_points.append([new_x, new_y])
    return new_points


def rotate_directional_polygon(x, y, points, a):
    new_points = []
    for point in points:
        dist = point[1]
        direction = point[0] + a
        new_x = x + math.cos(math.pi / 180 * direction) * dist
        new_y = y + math.sin(math.pi / 180 * direction) * dist
        new_points.append([new_x, new_y])
    return new_points


def convert_to_direction(points):
    new_points = []
    for point in points:
        dist = math.hypot(point[0], point[1])
        direction = to_point(0, 0, point[0], point[1])
        new_points.append([direction, dist])
    return new_points


def check_intersection(points, points2):
    pol = Polygon(points.copy())
    pol2 = Polygon(points2.copy())
    return pol.intersects(pol2)


def check_point_intersection(points, point):
    pol = Polygon(points)
    return pol.contains(point)