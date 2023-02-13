import pygame
import sys
from buttons_menu import Btn
from main import Game
from sandbox import Sandbox as Sbox
from AnimSpites import Font

pygame.init()
pygame.mixer.init()
cnf_snd = pygame.mixer.Sound('data/Confirm 1.wav')
pygame.mixer.music.load('data/menumusic.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('Project 7255')
BG = pygame.image.load('data/background.jpg')
img = pygame.image.load('data/logopng.png')
img.convert_alpha()


class main_menu:
    def options():
        while True:
            st_ms_pos = pygame.mouse.get_pos()
            # Позиция мышки в настройках.
            screen.fill('#a3b4d6')
            ST_TEXT = Font.new_font(50).render('Настройка звука', True,
                                                 '#6600ff')
            ST_RECT = ST_TEXT.get_rect(center=(660, 100))
            VL_TEXT = Font.new_font(50).render(f'Текущая громкость - {round(pygame.mixer.music.get_volume() * 10)}', True,
                                                 '#6600ff')
            VL_RECT = VL_TEXT.get_rect(center=(660, 200))
            minus_button = Btn(img=pygame.image.load('data/test1.png'),
                            pos=(400, 400),
                            txt_inp='-', font=Font.new_font(75),
                            clr_base='#9933ff',
                            clr_hvr='#8000ff')
            plus_button = Btn(img=pygame.image.load('data/test1.png'),
                            pos=(850, 400),
                            txt_inp='+', font=Font.new_font(75),
                            clr_base='#9933ff',
                            clr_hvr='#8000ff')
            qt_button = Btn(img=pygame.image.load('data/test4.png'),
                            pos=(640, 550),
                            txt_inp='МЕНЮ', font=Font.new_font(75),
                            clr_base='#9933ff',
                            clr_hvr='#8000ff')
            screen.blit(ST_TEXT, ST_RECT)
            screen.blit(VL_TEXT, VL_RECT)

            for button in [minus_button, plus_button, qt_button]:
                button.changeColor(st_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if plus_button.checkForInput(st_ms_pos):
                        cnf_snd.play(   )
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
                    if minus_button.checkForInput(st_ms_pos):
                        cnf_snd.play()
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)
                    if qt_button.checkForInput(st_ms_pos):
                        cnf_snd.play()
                        main_menu.main_menu()

            pygame.display.update()

    def main_menu():
        while True:
            screen.blit(BG, (0, 0))
            screen.blit(img, (330, 20))
            menu_ms_pos = pygame.mouse.get_pos()
            pl_button = Btn(img=pygame.image.load('data/Play Rect.png'),
                            pos=(640, 250),
                            txt_inp='ИГРАТЬ', font=Font.new_font(75),
                            clr_base='#9933ff', clr_hvr='#8000ff')
            st_button = Btn(
                img=pygame.image.load('data/test2.png'), pos=(640, 400),
                txt_inp='НАСТРОЙКИ',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            qt_button = Btn(img=pygame.image.load('data/test1.png'),
                            pos=(640, 550),
                            txt_inp='ВЫЙТИ', font=Font.new_font(75), clr_base='#9933ff',
                            clr_hvr='#8000ff')

            for button in [pl_button, st_button, qt_button]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pl_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()
                    if st_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        main_menu.options()
                    if qt_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


class play_menu:
    def play_game(mapp):
        pygame.mixer.music.stop()
        Game.main(mapp)
        pygame.quit()
        exit()

    def sandbox(mapp):
        pygame.mixer.music.stop()
        Sbox.sandbox(mapp)
        pygame.quit()
        exit()


    def maps_sbox(mapp):
        while True:
            mapp = ''
            screen.blit(BG, (0, 0))
            menu_ms_pos = pygame.mouse.get_pos()
            MENU_TEXT = Font.new_font(50).render('Выберите карту.', True, '#6600ff')
            MENU_RECT = MENU_TEXT.get_rect(center=(660, 100))
            map1 = Btn(
                img=pygame.image.load('data/test1.png'), pos=(450, 250),
                txt_inp='Город',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            map2 = Btn(img=pygame.image.load('data/test1.png'),
                       pos=(850, 250),
                       txt_inp='Поле', font=Font.new_font(75), clr_base='#9933ff',
                       clr_hvr='#8000ff')
            qt_button = Btn(img=pygame.image.load('data/test4.png'),
                            pos=(640, 550),
                            txt_inp='МЕНЮ', font=Font.new_font(75),
                            clr_base='#9933ff',
                            clr_hvr='#8000ff')

            screen.blit(MENU_TEXT, MENU_RECT)
            for button in [map1, map2, qt_button]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if map1.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        mapp = 'map1.csv'
                        play_menu.sandbox(mapp)
                    if map2.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        mapp = 'map2.csv'
                        play_menu.sandbox(mapp)
                    if qt_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()

            pygame.display.update()

    def maps(mapp):
        while True:
            mapp = ''
            screen.blit(BG, (0, 0))
            menu_ms_pos = pygame.mouse.get_pos()
            MENU_TEXT = Font.new_font(50).render('Выберите карту.', True, '#6600ff')
            MENU_RECT = MENU_TEXT.get_rect(center=(660, 100))
            map1 = Btn(
                img=pygame.image.load('data/test1.png'), pos=(450, 250),
                txt_inp='Город',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            map2 = Btn(img=pygame.image.load('data/test1.png'),
                       pos=(850, 250),
                       txt_inp='Поле', font=Font.new_font(75), clr_base='#9933ff',
                       clr_hvr='#8000ff')
            qt_button = Btn(img=pygame.image.load('data/test4.png'),
                            pos=(640, 550),
                            txt_inp='МЕНЮ', font=Font.new_font(75),
                            clr_base='#9933ff',
                            clr_hvr='#8000ff')

            screen.blit(MENU_TEXT, MENU_RECT)
            for button in [map1, map2, qt_button]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if map1.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        mapp = 'map1.csv'
                        play_menu.play_game(mapp)
                    if map2.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        mapp = 'map2.csv'
                        play_menu.play_game(mapp)
                    if qt_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()

            pygame.display.update()

    def menu():
        while True:
            screen.blit(BG, (0, 0))
            screen.blit(img, (330, 20))
            menu_ms_pos = pygame.mouse.get_pos()
            pl_button = Btn(img=pygame.image.load('data/Play Rect.png'),
                            pos=(640, 250),
                            txt_inp='ИГРАТЬ', font=Font.new_font(75),
                            clr_base='#9933ff', clr_hvr='#8000ff')
            st_button = Btn(
                img=pygame.image.load('data/test2.png'), pos=(640, 400),
                txt_inp='ПЕСОЧНИЦА',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            qt_button = Btn(img=pygame.image.load('data/test4.png'),
                            pos=(640, 550),
                            txt_inp='МЕНЮ', font=Font.new_font(75), clr_base='#9933ff',
                            clr_hvr='#8000ff')

            for button in [pl_button, st_button, qt_button]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pl_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.maps('')
                    if st_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.maps_sbox('')
                    if qt_button.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        main_menu.main_menu()

            pygame.display.update()



main_menu.main_menu()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()
