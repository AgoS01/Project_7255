from sprites import Sp
import pygame
import sys
# from menu_buttons import main_menu
# from buttons_menu import Btn


class victory:
    pygame.init()

    def gr_win():
        img = pygame.image.load('data/green_won.png')
        screen = pygame.display.set_mode((1280, 800))
        screen.blit(img, (330, 20))
        menu_ms_pos = pygame.mouse.get_pos()
        menu_back = Btn(img=None, pos=(640, 460), txt_inp='Вернуться в меню',
                        font=Font.new_font(75), clr_base='#9933ff',
                        clr_hvr='#8000ff')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_back.checkForInput(menu_ms_pos):
                    main_menu.options()

        pygame.display.update()

    def rd_win():
        img = pygame.image.load('data/red_won.png')
        screen = pygame.display.set_mode((1280, 800))
        screen.blit(img, (330, 20))
        menu_ms_pos = pygame.mouse.get_pos()
        menu_back = Btn(img=None, pos=(640, 460), txt_inp='Вернуться в меню',
                        font=Font.new_font(75), clr_base='#9933ff',
                        clr_hvr='#8000ff')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_back.checkForInput(menu_ms_pos):
                    main_menu.options()

        pygame.display.update()


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