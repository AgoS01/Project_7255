import pygame
import sys
from buttons_menu import Btn
from main import Game as gm

pygame.init()
pygame.mixer.init()
my_sound = pygame.mixer.Sound('data/Confirm 1.wav')
pygame.mixer.music.load('data/menumusic.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('Project 7255')
BG = pygame.image.load('data/background.jpg')
img = pygame.image.load('data/logopng.png')
img.convert_alpha()


def new_font(size):
    return pygame.font.Font('data/font2.ttf', size)


def menu():
    while True:
        screen.blit(BG, (0, 0))
        screen.blit(img, (330, 20))
        menu_ms_pos = pygame.mouse.get_pos()
        # MENU_TEXT = new_font(100).render('Project 7720', True, '#6600ff')
        # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        pl_button = Btn(img=pygame.image.load('data/Play Rect.png'),
                        pos=(640, 250),
                        txt_inp='ИГРАТЬ', font=new_font(75),
                        clr_base='#9933ff', clr_hvr='#8000ff')
        st_button = Btn(
            img=pygame.image.load('data/test2.png'), pos=(640, 400),
            txt_inp='ПЕСОЧНИЦА',
            font=new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
        qt_button = Btn(img=pygame.image.load('data/test4.png'),
                        pos=(640, 550),
                        txt_inp='МЕНЮ', font=new_font(75), clr_base='#9933ff',
                        clr_hvr='#8000ff')

        # screen.blit(MENU_TEXT, MENU_RECT)

        for button in [pl_button, st_button, qt_button]:
            button.changeColor(menu_ms_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pl_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    maps('')
                if st_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    options()
                if qt_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    main_menu()

        pygame.display.update()
    # pygame.mixer.music.stop()
    # gm.main()
    # pygame.quit()
    # exit()


def play_game(mapp):
    pygame.mixer.music.stop()
    gm.main(mapp)
    pygame.quit()
    exit()


def options():
    while True:
        st_ms_pos = pygame.mouse.get_pos()
        # Позиция мышки в настройках.
        screen.fill('#a3b4d6')
        st_text = new_font(45).render('В разработке.', True,
                                      'Black')
        st_rect = st_text.get_rect(center=(640, 260))
        screen.blit(st_text, st_rect)
        st_back = Btn(img=None, pos=(640, 460), txt_inp='Вернуться в меню',
                      font=new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
        st_back.changeColor(st_ms_pos)
        st_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if st_back.checkForInput(st_ms_pos):
                    my_sound.play()
                    main_menu()

        pygame.display.update()


def maps(mapp):
    while True:
        mapp = ''
        screen.blit(BG, (0, 0))
        menu_ms_pos = pygame.mouse.get_pos()
        MENU_TEXT = new_font(50).render('Выберите карту.', True, '#6600ff')
        MENU_RECT = MENU_TEXT.get_rect(center=(660, 100))
        map1 = Btn(
            img=pygame.image.load('data/test1.png'), pos=(450, 250),
            txt_inp='Город',
            font=new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
        map2 = Btn(img=pygame.image.load('data/test1.png'),
                        pos=(850, 250),
                        txt_inp='Поле', font=new_font(75), clr_base='#9933ff',
                        clr_hvr='#8000ff')

        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [map1, map2]:
            button.changeColor(menu_ms_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map1.checkForInput(menu_ms_pos):
                    my_sound.play()
                    mapp = 'map1.csv'
                    play_game(mapp)
                if map2.checkForInput(menu_ms_pos):
                    my_sound.play()
                    mapp = 'map2.csv'
                    play_game(mapp)

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        screen.blit(img, (330, 20))
        menu_ms_pos = pygame.mouse.get_pos()
        # MENU_TEXT = new_font(100).render('Project 7720', True, '#6600ff')
        # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        pl_button = Btn(img=pygame.image.load('data/Play Rect.png'),
                        pos=(640, 250),
                        txt_inp='ИГРАТЬ', font=new_font(75),
                        clr_base='#9933ff', clr_hvr='#8000ff')
        st_button = Btn(
            img=pygame.image.load('data/test2.png'), pos=(640, 400),
            txt_inp='НАСТРОЙКИ',
            font=new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
        qt_button = Btn(img=pygame.image.load('data/test1.png'),
                        pos=(640, 550),
                        txt_inp='ВЫЙТИ', font=new_font(75), clr_base='#9933ff',
                        clr_hvr='#8000ff')

        # screen.blit(MENU_TEXT, MENU_RECT)

        for button in [pl_button, st_button, qt_button]:
            button.changeColor(menu_ms_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pl_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    menu()
                if st_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    options()
                if qt_button.checkForInput(menu_ms_pos):
                    my_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()
