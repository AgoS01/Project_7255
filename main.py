import os
import sys
import pygame
import csv


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
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + i * self.cell_size, self.top + j * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

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
        all_sprites.add(self)

    def load_image(self, colorkey = None):
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
            map1 = list(reader)
            map1[0][0] = map1[0][0][-1:]
            self.map1 = map1


    def on_click(self, cell):
        '''self.board[cell[0]][cell[1]] = (self.board[cell[0]][cell[1]] + 1) % 2'''

    def render(self, screen):
        '''for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y]:
                    pygame.draw.rect(screen, pygame.Color("green"),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (x * self.cell_size + self.left,
                                                                       y * self.cell_size + self.top, self.cell_size,
                                                                       self.cell_size), 1)'''

    def first_render(self, screen):
        self.map_sp = [[None] * (self.width) for i in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                n = self.map1[y][x]
                if int(n) > 4:
                    n = '0'
                self.map_sp[y][x] = Sp(f'{n}.png')
                self.map_sp[y][x].rect.left = self.left + x * self.cell_size
                self.map_sp[y][x].rect.top = self.top + y * self.cell_size



    def next_move(self):
        '''tmp_board = copy.deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                s = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                            continue
                        s += self.board[y + dy][x + dx]
                s -= self.board[y][x]
                if s == 3:
                    tmp_board[y][x] = 1
                if s < 2 or s > 3:
                    tmp_board[y][x] = 0
        self.board = copy.deepcopy(tmp_board)'''



def main():
    pygame.init()
    pygame.display.set_caption('игра в жизнь')
    size = width, height = 1920*3/4, 1080*3/4
    screen = pygame.display.set_mode(size)
    board = main_board(11, 11, 100, 10, 70, 'map1.csv')
    board.set_view(300, 10, 70)
    running = True
    time_on = False
    speed = 15
    ticks = 0
    clock = pygame.time.Clock()
    main_board.map_sp = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, "#3b1604", (board.left, board.top, board.cell_size * board.width, board.cell_size * board.height))
        board.first_render(screen)
        main_board.map_sp.draw(screen)
        all_sprites.draw(screen)
        if ticks >= speed:
            if time_on:
                board.next_move()
            ticks = 0
        pygame.display.flip()
        clock.tick(100)
        ticks += 1
    pygame.quit()


if __name__ == "__main__":
    all_sprites = pygame.sprite.Group()
    main()