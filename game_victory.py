import pygame
import sys
from buttons_menu import Btn
from menu_buttons import Font

pygame.init()
screen = pygame.display.set_mode((1280, 800))


def gr_win():
    img = pygame.image.load('data/green_won.png')
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
                pygame.quit()
                sys.exit()
                # main_menu.options()

    pygame.display.update()


def rd_win():
    img = pygame.image.load('data/red_won.png')
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
                pygame.quit()
                sys.exit()
                # main_menu.options()

    pygame.display.update()