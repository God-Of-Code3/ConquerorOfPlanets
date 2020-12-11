from Classes.Constants import *
import math


def check_point(info, x, y):

    s_x = info["x"]
    s_y = info["y"]
    w = info["width"]
    print(s_x, s_y)
    print(x, y)
    return math.sqrt((s_x - x) ** 2 + (s_y - y) ** 2) <= w


class Planet:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class Starship:
    def __init__(self, x, y, width, height, ship_type, planet, health=1000, image="Ship1.png"):
        self.x = x  # Градус относительно "верха" планеты
        self.y = y  # Высота НАД ПОВЕРХНОСТЬЮ ПЛАНЕТЫ
        self.width = width  # Ширина коробля
        self.height = height  # Высота корабля
        self.energy = 1000  # Показатель энергии
        if ship_type in STARSHIPS:  # Если существует тип корабля, то берем данные из него
            self.type = ship_type  # Тип корабля (название)
            ship = STARSHIPS[ship_type]
            self.health = ship["health"]  # Прочность корабля
            self.image = ship["image"]  # Картинка корабля
        else:  # Иначе из переданных значений
            self.type = "Пользовательский"
            self.health = health  # Прочность корабля
            self.image = image  # Картинка корабля
        self.planet = planet  # Объект планеты
        self.speed_x = 0  # Текущая угловая скорость
        self.speed_y = 0  # Текущая скорость удаления от планеты
        self.ship_speed_x = 0.1  # Угловая скорость для этого корабля
        self.ship_speed_y = 1  # Скорость удаления от планеты для этого корабля

    def accelerate(self, x_direction, y_direction):  # Ускорение/замедление
        self.speed_x = self.ship_speed_x * x_direction  # Изменение параметров текущей скорости
        self.speed_y = self.ship_speed_y * y_direction

    def move(self):  # Движение
        self.x += self.speed_x  # Движение над планетой
        self.y += self.speed_y  # Движение от/к планете

    def check_colision(self, other):
        other_coords = other.get_real_coords()
        intersection = check_point(self.get_info_for_drawing(), other_coords[0], other_coords[1])

        return intersection

    def get_points(self):
        self_points = list()
        x, y = self.get_real_coords()
        self_points.append((x-self.width / 2, y-self.height / 2))
        self_points.append((x+self.width / 2, y-self.height / 2))
        self_points.append((x+self.width / 2, y+self.height / 2))
        self_points.append((x-self.width / 2, y+self.height / 2))
        return self_points

    def get_real_coords(self):
        start_x = self.planet.x  # Начальный X
        start_y = self.planet.y  # Начальный Y
        abs_x = start_x + math.cos((math.pi / 180) * self.x) * (self.y + self.planet.radius)  # Абсолютное значение
        # X (от левого верхнего края экрана)
        abs_y = start_y + math.sin((math.pi / 180) * self.x) * (self.y + self.planet.radius)
        return abs_x, abs_y

    def do(self):  # Общий расчет корабля
        self.move()

    def get_info_for_drawing(self):  # Выдача информации для отрисовки
        start_x = self.planet.x  # Начальный X
        start_y = self.planet.y  # Начальный Y
        abs_x = start_x + math.cos((math.pi / 180) * self.x) * (self.y + self.planet.radius)  # Абсолютное значение
        # X (от левого верхнего края экрана)
        abs_y = start_y + math.sin((math.pi / 180) * self.x) * (self.y + self.planet.radius)
        data = dict()  # Словарь данных
        data["x"] = abs_x
        data["y"] = abs_y
        data["image"] = self.image
        data["width"] = self.width
        data["height"] = self.height
        data["rot"] = self.x % 360
        return data


planet = Planet(0, 0, 0)
starship = Starship(0, 10, 2, 5, "Ship1", planet)
starship2 = Starship(0, 11, 2, 5, "Ship1", planet)
print(starship.check_colision(starship2))