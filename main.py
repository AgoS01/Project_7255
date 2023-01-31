import os
import sys
import pygame
import csv
import copy


class Board:
    # создание поля
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pass

    def on_click(self, mouse_pos):
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Sp(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = self.load_image()
        self.rect = self.image.get_rect()

    def load_image(self, colorkey=None):
        fullname = os.path.join('data', self.name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


class main_board(Board):
    def __init__(self, width, height, left, top, cell_size, f_name):
        super().__init__(width, height, left, top, cell_size)
        with open(f'data/{f_name}', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            map1 = list(reader)  # импрот карты из csv файла
            map1[0][0] = map1[0][0][-1:]
            self.map = map1  # карта неподвижного
            self.map_mas = [[None] * self.width for _ in range(self.height)]  # массив неподвижых спрайтов
            self.moving_map = [[None] * self.width for _ in range(self.height)]  # карта подвижного
            self.moving_map_mas = [[None] * self.width for _ in range(self.height)]  # массив подвижых спрайтов
            self.map_sp = pygame.sprite.Group()
            self.pieces_sp = pygame.sprite.Group()
            self.extra_sp = pygame.sprite.Group()
            self.focused = Sp('focused.png')
            self.focused_cell = None
            self.dest = 0, 0

    def on_click(self, cell):
        self.extra_sp.empty()
        if self.moving_map[cell[1]][cell[0]] in ('11', '12'):
            self.focused = Sp('focused_3.png')
            self.focused.rect.left = self.left + (cell[0] - 1) * self.cell_size
            self.focused.rect.top = self.top + cell[1] * self.cell_size
            self.extra_sp.add(self.focused)
        elif self.moving_map[cell[1]][cell[0]] in ('5', '6', '7', '8', '9', '10'):  # что можно выделять
            self.focused = Sp('focused.png')
            self.focused.rect.left = self.left + cell[0] * self.cell_size
            self.focused.rect.top = self.top + cell[1] * self.cell_size
            self.extra_sp.add(self.focused)
        self.focused_cell = cell

    def render(self, screen):
        try:
            if self.dest != (0, 0): # если перемещение есть
                if (self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + self.dest[0]] is None
                        and self.map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + self.dest[0]] not in (
                                '1', '2', '3', '5', '6') and 0 <= self.focused_cell[1] + self.dest[1] <= self.height and
                        0 <= self.focused_cell[0] + self.dest[0] <= self.width and self.moving_map[self.focused_cell[1]
                        ][self.focused_cell[0]] not in ('5', '6')):
                    if self.moving_map[self.focused_cell[1]][self.focused_cell[0]] in ('11', '12'):
                        if (self.dest[1] == 0 and self.map[self.focused_cell[1] + self.dest[1] * 2][self.focused_cell[0]
                                + self.dest[0] * 2] not in (
                                '1', '2', '3', '5', '6') and 0 <= self.focused_cell[1] +
                                self.dest[1] * 2 <= self.height and 0 <= self.focused_cell[0] +
                                self.dest[0] * 2 <= self.width and self.moving_map[self.focused_cell[1] + self.dest[1]][
                                self.focused_cell[0] + self.dest[0] * 2] is None):
                            new_cell = self.focused_cell[1] + self.dest[1], self.focused_cell[0] + self.dest[0]
                            self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + \
                                                                                 self.dest[0]] = \
                                self.moving_map[self.focused_cell[1]][self.focused_cell[0]]
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0]] = None
                            self.on_click((new_cell[1], new_cell[0]))
                            self.dest = 0, 0
                    else:
                        if not (self.dest[1] == 0 and (self.focused_cell[0] in (1, 9) or self.focused_cell[1] in (0, 10) # где-то здесь ошибка
                            ) or (self.dest[0] == 0 and
                                  (self.focused_cell[1] in (1, 9) or self.focused_cell[0] in (0, 10)))):
                            if (self.dest[1] == 0 and (self.moving_map[self.focused_cell[1] + self.dest[1]][ # условия на то,что так не въезжает в поезд
                                    self.focused_cell[0] + self.dest[0] * 2] not in ('11', '12') and
                                    self.moving_map[self.focused_cell[1] + self.dest[1] * 2][
                                    self.focused_cell[0] + self.dest[0]] not in ('11', '12')) or
                                    (self.dest[0] == 0 and
                                    self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] - 1]
                                    not in ('11', '12') and self.moving_map[self.focused_cell[1] + self.dest[1]][
                                    self.focused_cell[0] + 1] not in ('11', '12'))):
                                new_cell = self.focused_cell[1] + self.dest[1], self.focused_cell[0] + self.dest[0]
                                self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + \
                                    self.dest[0]] = self.moving_map[self.focused_cell[1]][self.focused_cell[0]]
                                self.moving_map[self.focused_cell[1]][self.focused_cell[0]] = None
                                self.on_click((new_cell[1], new_cell[0]))
                                self.dest = 0, 0
                        else:
                            new_cell = self.focused_cell[1] + self.dest[1], self.focused_cell[0] + self.dest[0]
                            self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + \
                                                                                 self.dest[0]] = \
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0]]
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0]] = None
                            self.on_click((new_cell[1], new_cell[0]))
                            self.dest = 0, 0
        except IndexError:
            pass
        self.pieces_sp.empty()
        for y in range(self.height):
            for x in range(self.width):
                n = self.moving_map[y][x]
                if n and n not in ('11', '12'):
                    self.moving_map_mas[y][x] = Sp(f'{n}.png')
                    self.moving_map_mas[y][x].rect.left = self.left + x * self.cell_size
                    self.moving_map_mas[y][x].rect.top = self.top + y * self.cell_size
                    self.pieces_sp.add(self.moving_map_mas[y][x])
                elif n in ('11', '12'):
                    self.moving_map_mas[y][x] = Sp(f'{n}.png')
                    self.moving_map_mas[y][x].rect.left = self.left + (x - 1) * self.cell_size
                    self.moving_map_mas[y][x].rect.top = self.top + y * self.cell_size
                    self.pieces_sp.add(self.moving_map_mas[y][x])
        self.pieces_sp.draw(screen)

    def first_render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                n = self.map[y][x]
                if n == '12' or n == '11':
                    self.moving_map[y][x] = n
                    n = '11_1'
                if int(n) > 4 and n != '11_1':  # если подвижый элемент, нарисуй землю
                    self.moving_map[y][x] = n
                    n = '0'
                self.map[y][x] = n
                self.map_mas[y][x] = Sp(f'{n}.png')  # создание спрайта с номером из csv-карты
                self.map_mas[y][x].rect.left = self.left + x * self.cell_size
                self.map_mas[y][x].rect.top = self.top + y * self.cell_size
                self.map_sp.add(self.map_mas[y][x])

    def next_move(self):
        pass


def main():
    pygame.init()
    pygame.display.set_caption('Игра')
    size = width, height = 1920 * 3 / 4, 1080 * 3 / 4
    screen = pygame.display.set_mode(size)
    board = main_board(11, 11, 100, 10, 70, 'map1.csv')
    board.set_view(300, 10, 70)
    board.first_render(screen)
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    running = True
    time_on = False
    speed = 15
    ticks = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.dest = 0, 0
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN and board.focused_cell:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    board.dest = 0, -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    board.dest = 0, 1
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    board.dest = -1, 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    board.dest = 1, 0
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, "#d55800", (
            board.left, board.top, board.cell_size * board.width, board.cell_size * board.height))  # подложка
        board.map_sp.draw(screen)  # создание карты
        board.render(screen)
        board.extra_sp.draw(screen)
        if ticks >= speed:
            if time_on:
                board.next_move()
            ticks = 0
        pygame.display.flip()
        clock.tick(10)
        ticks += 1
    pygame.quit()


if __name__ == "__main__":
    all_sprites = pygame.sprite.Group()
    main()
