import pygame


SIZE = (500, 500)


class Camera:
    def __init__(self, color): # Определения класса
        self.color = color
    
    def fill(self, screen):
        screen.fill(self.color) # Установка цвета фона
    
    def render(self):
        pygame.display.flip() # Обновление экрана
        
    def drawing(self, screen, objects, center, size): # center - кортеж с x и y камеры
        # Отрисовка списков словарей
        for v in objects:
            img = pygame.image.load(v['image']) # Открытие картинки
            img = pygame.transform.scale(img, (int(v['width'] * size),
                                               int(v['height'] * size))) # Изменение размера картинки
            img = pygame.transform.rotate(img, -v['rot']) # Поворот картинки
            screen.blit(img, (SIZE[0] / 2 + (v['x'] - v['width'] / 2 - center[0]) * size,
                              SIZE[1] / 2 + (v['y'] - v['height'] / 2 - center[1]) * size)) # Отрисовка
            
# Дальше типа пример          
'''if __name__ == '__main__':
    pygame.init()
    size = width, height = SIZE[0], SIZE[1]
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    
    cam = Camera(pygame.Color('black'))
    running = True
    a = 0.5
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and a < 5:
                    a += 0.1
                elif event.button == 3 and a > 0.2:
                    a -= 0.1
        cam.fill(screen)
        cam.drawing(screen, [{"x": -100, "y": 100, "image": "1.png", "width": 100, "height": 150, "rot": 45},
                             {"x": 100, "y": -100, "image": "2.png", "width": 120, "height": 70, "rot": 55}],
                    (250, 250), a)
        cam.render()
    
    pygame.quit()'''
