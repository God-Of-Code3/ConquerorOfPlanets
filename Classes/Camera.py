import pygame


SIZE = (500, 500)
SENSITIVITY = 2
ZOOM_SENSITIVITY = 1.2


class Camera:
    def __init__(self, color): # Определения класса
        self.color = color
        self.cam_pos = (0, 0)
        self.zoom_value = 1

    def moving(self, x, y):  # Движение камеры
        self.cam_pos = (self.cam_pos[0] + x, self.cam_pos[1] + y)

    def get_position(self):  # Взять позицию
        return self.cam_pos

    def zoom(self, value):  # Приближение
        if 3 > self.zoom_value * value > 0.1:
            self.zoom_value *= value

    def get_zoom(self):  # Взять приближение
        return self.zoom_value

    def fill(self, screen):
        screen.fill(self.color)  # Установка цвета фона
    
    def render(self):
        pygame.display.flip()  # Обновление экрана
        
    def drawing(self, screen, objects, center, zoom): # center - кортеж с x и y камеры
        # Отрисовка списков словарей
        for v in objects:
            img = pygame.image.load(v['image']) # Открытие картинки
            img = pygame.transform.scale(img, (int(v['width'] * zoom),
                                               int(v['height'] * zoom))) # Изменение размера картинки
            img = pygame.transform.rotate(img, -v['rot']) # Поворот картинки
            screen.blit(img, (SIZE[0] / 2 + (v['x'] - v['width'] / 2 - center[0]) * zoom,
                              SIZE[1] / 2 + (v['y'] - v['height'] / 2 - center[1]) * zoom)) # Отрисовка
            
# Дальше типа пример
if __name__ == '__main__':
    pygame.init()
    size = width, height = SIZE[0], SIZE[1]
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))

    W = A = S = D = False # Зажаты ли клавиши
    cam = Camera(pygame.Color('blue')) # Создание камеры
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Изменение зума
                if event.button == 4:
                    cam.zoom(ZOOM_SENSITIVITY)
                elif event.button == 5:
                    cam.zoom(1 / ZOOM_SENSITIVITY)
            if event.type == pygame.KEYDOWN: # Зажатие клавиш
                if event.key == ord('w'):
                    W = True
                if event.key == ord('a'):
                    A = True
                if event.key == ord('s'):
                    S = True
                if event.key == ord('d'):
                    D = True
            if event.type == pygame.KEYUP: # Отжатие клавиш
                if event.key == ord('w'):
                    W = False
                if event.key == ord('a'):
                    A = False
                if event.key == ord('s'):
                    S = False
                if event.key == ord('d'):
                    D = False
        cam.fill(screen)
        if W: # Движение
            cam.moving(0, -SENSITIVITY)
        if A:
            cam.moving(-SENSITIVITY, 0)
        if S:
            cam.moving(0, SENSITIVITY)
        if D:
            cam.moving(SENSITIVITY, 0)
        cam.drawing(screen, [{"x": -100, "y": 100, "image": "1.png", "width": 100, "height": 150, "rot": 45},
                             {"x": 100, "y": -100, "image": "2.png", "width": 120, "height": 70, "rot": 55}],
                    cam.get_position(), cam.get_zoom())
        cam.render()
    
    pygame.quit()

