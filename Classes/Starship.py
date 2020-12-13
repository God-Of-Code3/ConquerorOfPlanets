from Classes.Constants import *
from Classes.Math import *
import pygame


def check_point(info, x, y):

    s_x = info["x"]
    s_y = info["y"]
    w = info["width"]
    print(s_x, s_y)
    print(x, y)
    return math.sqrt((s_x - x) ** 2 + (s_y - y) ** 2) <= w


class Starship:
    def __init__(self, x, y, width, height, ship_type, planet, health=1000, image="Ship1.png", polygon=[]):
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
            self.polygon = ship["polygon"]  # Полигон корабля
        else:  # Иначе из переданных значений
            self.type = "Пользовательский"
            self.health = health  # Прочность корабля
            self.image = image  # Картинка корабля
            self.polygon = polygon.copy()  # Полигон корабля
        self.planet = planet  # Объект планеты
        self.speed_x = 0  # Текущая угловая скорость
        self.speed_y = 0  # Текущая скорость удаления от планеты
        self.ship_speed_x = 0.1  # Угловая скорость для этого корабля
        self.ship_speed_y = 2  # Скорость удаления от планеты для этого корабля
        self.img = pygame.image.load(self.image)

    def accelerate_x(self, x_direction):  # Ускорение/замедление
        self.speed_x = self.ship_speed_x * x_direction  # Изменение параметров текущей скорости

    def accelerate_y(self, y_direction):  # Ускорение/замедление
        self.speed_y = self.ship_speed_y * y_direction  # Изменение параметров текущей скорости

    def move(self):  # Движение
        self.x += self.speed_x / ((self.y + self.planet.radius) / (20 + self.planet.radius))  # Движение над планетой
        self.y += self.speed_y  # Движение от/к планете
        if self.y < self.height:
            self.y = self.height

    def get_my_polygon(self):
        abs_x, abs_y = self.get_real_coords()
        return rotate_polygon(abs_x, abs_y, self.polygon, self.x)

    def check_colision(self, other):
        intersection = check_intersection(self.get_my_polygon(), other.get_my_polygon())
        return intersection

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
        data["image"] = self.img
        data["width"] = self.width
        data["height"] = self.height
        polygon = rotate_polygon(0, 0, [[-self.width / 2, -self.height / 2], [self.width / 2, -self.height / 2],
                                        [self.width / 2, self.height / 2],
                                        [-self.width / 2,self.height / 2]], (self.x - 270) % 360)
        min_x = min(polygon, key=lambda x: x[0])
        max_x = max(polygon, key=lambda x: x[0])
        min_y = min(polygon, key=lambda x: x[1])
        max_y = max(polygon, key=lambda x: x[1])
        width = max_x[0] - min_x[0]
        height = max_y[1] - min_y[1]
        data["real_width"] = width
        data["real_height"] = height
        data["rot"] = (self.x - 270) % 360
        return data


"""
planet = Planet(250, 250, 0)
starship = Starship(0, 110, 2, 5, "Ship1", planet)
starship2 = Starship(45, 110, 2, 5, "Ship1", planet)


pygame.init()
screen = pygame.display.set_mode((500, 500))
while True:
    screen.fill((0, 0, 0))
    inter = starship.check_colision(starship2)
    color = (255, 0, 0) if inter else (255, 255, 255)
    print(starship.get_real_coords())
    pygame.draw.polygon(screen, color, starship.get_my_polygon(), 2)
    pygame.draw.polygon(screen, color, starship2.get_my_polygon(), 2)
    starship.x += 0.02
    starship2.x += 0.04
    pygame.display.flip()
    pygame.event.get()
"""
