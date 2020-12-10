from Classes.Constants import *
import math


def check_point(info, x, y):

    s_x = info["x"]
    s_y = info["y"]
    w = info["width"]
    h = info["height"]
    r = info["rot"]

    point_x = round(((x - s_x) * math.cos(math.pi / 180 * (-r)) -
                    (y - s_y) * math.sin(math.pi / 180 * (-r))) * 100) / 100
    point_y = round(((x - s_x) * math.sin(math.pi / 180 * (-r)) +
                    (y - s_y) * math.cos(math.pi / 180 * (-r))) * 100) / 100

    return -w/2 <= point_x <= w/2 and -h/2 <= point_y <= h/2
    # Пишу это в половине первого ночи, как работает эта математика - хз, но она работает


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
        pass

    def check_point(self, x, y):
        points = list()
        pass

    def do(self):  # Общий расчет корабля
        self.move()

    def get_info_for_drawing(self):  # Выдача информации для отрисовки
        start_x = self.planet.x  # Начальный X
        start_y = self.planet.y  # Начальный Y
        abs_x = start_x + math.cos((math.pi / 180) * self.x)  # Абсолютное значение X (от левого верхнего края экрана)
        abs_y = start_y + math.sin((math.pi / 180) * self.y)
        data = dict()  # Словарь данных
        data["x"] = abs_x
        data["y"] = abs_y
        data["image"] = self.image
        data["width"] = self.width
        data["height"] = self.height
        data["rot"] = self.x % 360
        return data


info = {"x": 0, "y": 0, "width": 2, "height": 2, "rot": 45}
check_point(info, 1.1, 0)