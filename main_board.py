from board import Board
import pygame
import csv
from sprites import Sp
from game_victory import victory

class MainBoard(Board):
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
            self.focused_cell = [-1, -1]
            self.dest = 0, 0
            self.rot = 0
            self.hit = -1, -1
            self.c = -1
            self.chosen = 0
            self.bull_dest = 0, 0
            self.bullet_ex = 0
            self.player = 0
            self.bullet_speed = 30
            self.rot_mas = {'7':180,'8':0,'9':270,'10':90,'5':270,'6':90}

    def player_move(self, cell):
        if self.player == 0:
            if self.moving_map[cell[1]][cell[0]] == '12.2':
                self.extra_sp.empty()
                self.focused = Sp('focused_3.png')
                self.chosen = 1
                self.focused_cell = cell
                self.focused.rect.left = self.left + (cell[0] - 1) * self.cell_size
                self.focused.rect.top = self.top + cell[1] * self.cell_size
                self.extra_sp.add(self.focused)
            elif self.moving_map[cell[1]][cell[0]] in ('6', '8', '10'):  # что можно выделять
                self.extra_sp.empty()
                self.focused = Sp('focused.png')
                self.focused_cell = cell
                self.focused.rect.left = self.left + cell[0] * self.cell_size
                self.focused.rect.top = self.top + cell[1] * self.cell_size
                self.extra_sp.add(self.focused)
                self.chosen = 1
        elif self.player == 1:
            if self.moving_map[cell[1]][cell[0]] == '11.2':
                self.extra_sp.empty()
                self.focused = Sp('focused_3.png')
                self.focused_cell = cell
                self.focused.rect.left = self.left + (cell[0] - 1) * self.cell_size
                self.focused.rect.top = self.top + cell[1] * self.cell_size
                self.extra_sp.add(self.focused)
                self.chosen = 1
            elif self.moving_map[cell[1]][cell[0]] in ('5', '7', '9'):  # что можно выделять
                self.extra_sp.empty()
                self.focused = Sp('focused.png')
                self.focused_cell = cell
                self.focused.rect.left = self.left + cell[0] * self.cell_size
                self.focused.rect.top = self.top + cell[1] * self.cell_size
                self.extra_sp.add(self.focused)
                self.chosen = 1

    def on_click(self, cell):
        if self.moving_map[cell[1]][cell[0]]:
            if '.1' in self.moving_map[cell[1]][cell[0]]:
                self.on_click((cell[0] + 1, cell[1]))
            if '.3' in self.moving_map[cell[1]][cell[0]]:
                self.on_click((cell[0] - 1, cell[1]))
            self.player_move(cell)

    def move_ability(self):
        if self.chosen:
            try:
                # условия поезда
                if self.moving_map[self.focused_cell[1]][self.focused_cell[0]] and \
                        self.moving_map[self.focused_cell[1]][self.focused_cell[0]] in ('11.2', '12.2'):

                    self.dest = (-self.dest[1], self.dest[0])

                    if (self.dest[1] == 0 and self.map[self.focused_cell[1]][self.focused_cell[0] + self.dest[0] * 2] not
                            in ('1', '2', '3', '5', '6') and 0 <= self.focused_cell[0] + self.dest[0] * 2 <=
                        self.width and self.moving_map[self.focused_cell[1]][self.focused_cell[0] + self.dest[0] * 2] is
                            None):
                        new_cell = self.focused_cell[1] + self.dest[1], self.focused_cell[0] + self.dest[0]
                        self.moving_map[self.focused_cell[1]][self.focused_cell[0] + self.dest[0] + 1],\
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0] + self.dest[0]],\
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0] + self.dest[0] - 1] = \
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0] + 1],\
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0]], \
                            self.moving_map[self.focused_cell[1]][self.focused_cell[0] - 1]
                        self.moving_map[self.focused_cell[1]][self.focused_cell[0] - self.dest[0]] = None
                        self.on_click((new_cell[1], new_cell[0]))
                        self.dest = 0, 0
                #условия других движущихся об.
                elif self.rot and self.moving_map[self.focused_cell[1]][self.focused_cell[0]] not in ('11.2', '12.2') :
                    self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]] = \
                        (self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]] + self.rot) % 360
                    self.rot = 0
                elif self.dest != (0, 0): # если перемещение есть
                    if self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]] == 90:
                        self.dest = (self.dest[1], self.dest[0])
                    elif self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]] == 270:
                        self.dest = (-self.dest[1], -self.dest[0])
                    elif self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]] == 180:
                        self.dest = (-self.dest[0], -self.dest[1])
                    if (self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + self.dest[0]] is None
                            and self.map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + self.dest[0]] not in (
                                    '1', '2', '3', '5', '6') and 0 <= self.focused_cell[1] + self.dest[1] <= self.height - 1
                            and 0 <= self.focused_cell[0] + self.dest[0] <= self.width - 1 and self.moving_map[
                                self.focused_cell[1]][self.focused_cell[0]] not in ('5', '6')):
                                new_cell = self.focused_cell[1] + self.dest[1], self.focused_cell[0] + self.dest[0]
                                self.moving_map[self.focused_cell[1] + self.dest[1]][self.focused_cell[0] + \
                                                                                     self.dest[0]] = \
                                self.moving_map[self.focused_cell[1]][self.focused_cell[0]]
                                self.moving_map[self.focused_cell[1]][self.focused_cell[0]] = None
                                self.on_click((new_cell[1], new_cell[0]))

                self.dest = 0, 0
            except IndexError:
                pass

    def shoot(self):
        if self.moving_map[self.focused_cell[1]][self.focused_cell[0]] in ('5', '6', '7', '8') and self.chosen: # what can shoot
            if self.bullet_ex:
                self.extra_sp.remove(self.bullet)
                self.bullet_ex = 0
            tmp_dest = self.rot_mas[self.moving_map[self.focused_cell[1]][self.focused_cell[0]]]
            self.bullet_ex = 1
            if tmp_dest == 0:
                self.bull_dest = 0, -1
            elif tmp_dest == 90:
                self.bull_dest = -1, 0
            elif tmp_dest == 270:
                self.bull_dest = 1, 0
            elif tmp_dest == 180:
                self.bull_dest = 0, 1
            self.bullet = Sp('bullet.png')
            self.bullet.rect.left = self.left + self.focused_cell[0] * self.cell_size
            self.bullet.rect.top = self.top + self.focused_cell[1] * self.cell_size
            self.bullet.image = pygame.transform.rotate(self.bullet.image, tmp_dest)
            self.extra_sp.add(self.bullet)

    def endgame(self):
        if not ('7' in [j for i in self.moving_map for j in i] and '9' in [j for i in self.moving_map for j in i]):
            victory.gr_win()
        if not ('8' in [j for i in self.moving_map for j in i] and '10' in [j for i in self.moving_map for j in i]):
            victory.rd_win()

    def render(self, screen):
        self.screen = screen
        self.move_ability()
        self.dest = 0, 0
        self.pieces_sp.empty()
        if self.c: #counter for explosion existance time
            self.c -= 1
        else:
            self.c = -1
            self.extra_sp.remove(self.explosion)
        if self.hit[0] != -1:
            pygame.mixer.init()
            exl_snd = pygame.mixer.Sound('data/explode.mp3')
            exl_snd.play()
            temp_pos = self.moving_map[self.hit[1]][self.hit[0]]
            temp_pos2 = self.map[self.hit[1]][self.hit[0]]
            self.explosion = Sp('boom.png')
            self.explosion.rect.left = self.left + self.hit[0] * self.cell_size - 10
            self.explosion.rect.top = self.top + self.hit[1] * self.cell_size - 10
            self.extra_sp.add(self.explosion)
            if temp_pos in ('5', '6', '7', '8', '9', '10'):
                self.moving_map[self.hit[1]][self.hit[0]] = None
                self.rot_mas.pop(temp_pos)
            if temp_pos2 == '1':
                self.map[self.hit[1]][self.hit[0]] = '0'
            self.hit = -1, -1
            self.c = 10
        if self.bullet_ex:
            self.bullet.rect.left += self.bullet_speed * self.bull_dest[0]
            self.bullet.rect.top += self.bullet_speed * self.bull_dest[1]
            if self.top > self.bullet.rect.top or self.bullet.rect.top > self.top + (self.height - 1) * \
                    self.cell_size or 0 + self.left > self.bullet.rect.left or self.bullet.rect.left >\
                    (self.width - 1) * self.cell_size + self.left:
                self.extra_sp.remove(self.bullet)
                self.bullet_ex = 0
            tmp_cell = self.get_cell((self.bullet.rect.left + 30, self.bullet.rect.top + 30))
            if self.bullet_ex:
                if self.moving_map[tmp_cell[1]][tmp_cell[0]] in ('5', '6', '7', '8', '11.1', '11.2', '11.3',
                        '12.1', '12.2', '12.3', '9', '10', '1', '2') and self.moving_map[tmp_cell[1]][tmp_cell[0]] !=\
                        self.moving_map[self.focused_cell[1]][self.focused_cell[0]]:
                    self.extra_sp.remove(self.bullet)
                    self.bullet_ex = 0
                    self.hit = tmp_cell
                if self.map[tmp_cell[1]][tmp_cell[0]] in ('1', '2') and self.moving_map[tmp_cell[1]][tmp_cell[0]] !=\
                        self.moving_map[self.focused_cell[1]][self.focused_cell[0]]:
                    self.extra_sp.remove(self.bullet)
                    self.bullet_ex = 0
                    self.hit = tmp_cell


        for y in range(self.height):
            for x in range(self.width):
                n = self.moving_map[y][x]
                if n:
                    self.moving_map_mas[y][x] = Sp(f'{n}.png')
                    self.moving_map_mas[y][x].rect.left = self.left + x * self.cell_size
                    self.moving_map_mas[y][x].rect.top = self.top + y * self.cell_size
                    if n and n not in ('11.1', '11.2', '11.3', '12.1', '12.2', '12.3'):
                        self.moving_map_mas[y][x].image = pygame.transform.rotate(self.moving_map_mas[y][x].image,
                                                                                  self.rot_mas[n])
                    self.pieces_sp.add(self.moving_map_mas[y][x])
        self.pieces_sp.draw(screen)

    def first_render(self, screen):
        self.map_sp.empty()
        for y in range(self.height):
            for x in range(self.width):
                n = self.map[y][x]
                if n in ('11.1', '11.2', '11.3', '12.1', '12.2', '12.3'):
                    self.moving_map[y][x] = n

                    n = '11_1'
                elif int(n) > 4 and n != '11_1':  # если подвижый элемент, нарисуй землю
                    self.moving_map[y][x] = n
                    n = '0'
                self.map[y][x] = n
                self.map_mas[y][x] = Sp(f'{n}.png')  # создание спрайта с номером из csv-карты
                self.map_mas[y][x].rect.left = self.left + x * self.cell_size
                self.map_mas[y][x].rect.top = self.top + y * self.cell_size
                self.map_sp.add(self.map_mas[y][x])