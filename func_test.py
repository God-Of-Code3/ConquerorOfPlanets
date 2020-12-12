import math


def angle(x1, y1, x2, y2):
    cos_a = (x2 - x1) / math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    a = math.acos(cos_a) / (math.pi / 180)
    return a


a1 = angle(0, 0, 0, -1)
x = math.cos(math.pi / 180 * a1)
y = math.sin(math.pi / 180 * a1)
print(round(x * 100) / 100, round(y * 100) / 100)
a1 = angle(0, 0, -1, -1)
x = math.cos(math.pi / 180 * a1)
y = math.sin(math.pi / 180 * a1)
print(round(x * 100) / 100, round(y * 100) / 100)
a1 = angle(0, 0, -1, 0)
x = math.cos(math.pi / 180 * a1)
y = math.sin(math.pi / 180 * a1)
print(round(x * 100) / 100, round(y * 100) / 100)
a1 = angle(0, 0, -1, 1)
x = math.cos(math.pi / 180 * a1)
y = math.sin(math.pi / 180 * a1)
print(round(x * 100) / 100, round(y * 100) / 100)
a1 = angle(0, 0, 0, 1)
x = math.cos(math.pi / 180 * a1)
y = math.sin(math.pi / 180 * a1)
print(round(x * 100) / 100, round(y * 100) / 100)
