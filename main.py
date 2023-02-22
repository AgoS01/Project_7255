import pygame
import sys
from buttons_menu import Btn
from main_render import Game
from sandbox import Sandbox as Sbox
from AnimSpites import Font
from load_image import load_image, screen

pygame.init()
pygame.mixer.init()
cnf_snd = pygame.mixer.Sound('data/Confirm 1.wav')
pygame.mixer.music.load('data/shine.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('Project 7255')
BG = pygame.image.load('data/background.jpg')
logo = pygame.image.load('data/logopng.png')
logo.convert_alpha()


class main_menu:
    def options():
        while True:
            st_ms_pos = pygame.mouse.get_pos()
            # Позиция мышки в настройках.
            screen.fill('#a3b4d6')
            text_st = Font.new_font(50).render('Настройка звука', True,
                                               '#6600ff')
            rect_st = text_st.get_rect(center=(660, 100))
            text_vl = Font.new_font(50).render(
                f'Текущая громкость - '
                f'{round(pygame.mixer.music.get_volume() * 10)}',
                True,
                '#6600ff')
            rect_vl = text_vl.get_rect(center=(660, 200))
            text_msc = Font.new_font(15).render('Выбор мелодии', True,
                                                '#6600ff')
            rect_msc = text_msc.get_rect(center=(1180, 15))
            pl1_btn = Btn(img=pygame.image.load('data/fon2.png'),
                          pos=(1125, 55),
                          txt_inp='►',
                          font=Font.new_font(15),
                          clr_base='#ffffff',
                          clr_hvr="#ffffff")
            pl2_btn = Btn(img=pygame.image.load('data/da4.png'),
                          pos=(1180, 55),
                          txt_inp='►',
                          font=Font.new_font(15),
                          clr_base='#ffffff',
                          clr_hvr="#ffffff")
            pl3_btn = Btn(img=pygame.image.load('data/fon3.png'),
                          pos=(1235, 55),
                          txt_inp='►',
                          font=Font.new_font(15),
                          clr_base='#ffffff',
                          clr_hvr="#ffffff")
            minus_btn = Btn(img=pygame.image.load('data/test1.png'),
                            pos=(420, 400),
                            txt_inp='-', font=Font.new_font(75),
                            clr_base='#8000ff',
                            clr_hvr='#6600cc')
            plus_btn = Btn(img=pygame.image.load('data/test1.png'),
                           pos=(900, 400),
                           txt_inp='+', font=Font.new_font(75),
                           clr_base='#8000ff',
                           clr_hvr='#6600cc')
            qt_btn = Btn(img=pygame.image.load('data/test4.png'),
                         pos=(660, 550),
                         txt_inp='МЕНЮ', font=Font.new_font(75),
                         clr_base='#8000ff',
                         clr_hvr='#6600cc')
            screen.blit(text_st, rect_st)
            screen.blit(text_vl, rect_vl)
            screen.blit(text_msc, rect_msc)

            for button in [pl1_btn, pl2_btn, pl3_btn, minus_btn, plus_btn,
                           qt_btn]:
                button.changeColor(st_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pl1_btn.checkForInput(st_ms_pos):
                        pygame.mixer.music.load('data/shine.mp3')
                        pygame.mixer.music.play(-1)
                    if pl2_btn.checkForInput(st_ms_pos):
                        pygame.mixer.music.load('data/retro.mp3')
                        pygame.mixer.music.play(-1)
                    if pl3_btn.checkForInput(st_ms_pos):
                        pygame.mixer.music.load('data/landoffire.mp3')
                        pygame.mixer.music.play(-1)
                    if plus_btn.checkForInput(st_ms_pos):
                        cnf_snd.play()
                        pygame.mixer.music.set_volume(
                            pygame.mixer.music.get_volume() + 0.1)
                    if minus_btn.checkForInput(st_ms_pos):
                        cnf_snd.play()
                        if pygame.mixer.music.get_volume() <= 0.1:
                            pygame.mixer.music.set_volume(0)
                        pygame.mixer.music.set_volume(
                            pygame.mixer.music.get_volume() - 0.1)
                    if qt_btn.checkForInput(st_ms_pos):
                        cnf_snd.play()
                        main_menu.main_menu()

            pygame.display.update()

    def main_menu():
        clock = pygame.time.Clock()
        running = True
        timer_animation = pygame.USEREVENT
        pygame.time.set_timer(timer_animation, 10)
        all_sprites = pygame.sprite.Group()

        frames = ['1.tiff', '2.tiff', '3.tiff', '4.tiff',
                  '5.tiff', '6.tiff', '7.tiff', '8.tiff', '9.tiff',
                  '10.tiff', '11.tiff', '12.tiff', '13.tiff', '14.tiff',
                  '15.tiff', '16.tiff', '17.tiff', '18.tiff', '19.tiff',
                  '20.tiff', '21.tiff', '22.tiff', '23.tiff', '24.tiff',
                  '25.tiff', '26.tiff', '27.tiff', '28.tiff', '29.tiff',
                  '30.tiff', '31.tiff', '32.tiff', '33.tiff', '34.tiff',
                  '35.tiff', '36.tiff', '37.tiff', '38.tiff', '39.tiff',
                  '40.tiff', '41.tiff', '42.tiff', '43.tiff', '44.tiff',
                  '45.tiff', '46.tiff', '47.tiff', '48.tiff', '49.tiff',
                  '50.tiff', '51.tiff', '52.tiff', '53.tiff', '54.tiff',
                  '55.tiff', '56.tiff', '57.tiff', '58.tiff', '59.tiff',
                  '60.tiff', '61.tiff', '62.tiff', '63.tiff', '64.tiff',
                  '65.tiff', '66.tiff', '67.tiff', '68.tiff', '69.tiff',
                  '70.tiff', '71.tiff', '72.tiff', '73.tiff', '74.tiff',
                  '75.tiff', '76.tiff', '77.tiff', '78.tiff', '79.tiff',
                  '80.tiff', '81.tiff', '82.tiff', '83.tiff', '84.tiff',
                  '85.tiff', '86.tiff', '87.tiff', '88.tiff', '89.tiff',
                  '90.tiff', '91.tiff', '92.tiff', '93.tiff', '94.tiff',
                  '95.tiff', '96.tiff', '97.tiff', '98.tiff', '99.tiff',
                  '100.tiff', '101.tiff', '102.tiff', '103.tiff',
                  '104.tiff', '105.tiff', '106.tiff', '107.tiff',
                  '108.tiff', '109.tiff', '110.tiff', '111.tiff',
                  '112.tiff', '113.tiff', '114.tiff', '115.tiff',
                  '116.tiff', '117.tiff', '118.tiff', '119.tiff',
                  '120.tiff', '121.tiff', '122.tiff', '123.tiff',
                  '124.tiff', '125.tiff', '126.tiff', '127.tiff',
                  '128.tiff', '129.tiff', '130.tiff', '131.tiff',
                  '132.tiff', '133.tiff', '134.tiff', '135.tiff',
                  '136.tiff', '137.tiff', '138.tiff', '139.tiff',
                  '140.tiff', '141.tiff', '142.tiff', '143.tiff',
                  '144.tiff', '145.tiff', '146.tiff']

        cur_frame = 0
        background = pygame.sprite.Sprite()
        background.image = load_image(frames[cur_frame])
        background.image = pygame.transform.scale(background.image,
                                                  (1280, 800))
        background.rect = background.image.get_rect()
        background.rect.x = 0
        background.rect.y = 0
        while running:
            all_sprites.add(background)
            screen.blit(background.image, (0, 0))
            screen.blit(logo, (330, 40))
            menu_ms_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                if event.type == timer_animation:
                    cur_frame = (cur_frame + 1) % len(frames)
                    background.image = load_image(frames[cur_frame])
                    background.image = pygame.transform.scale(background.image,
                                                              (1280, 800))

            pl_btn = Btn(img=pygame.image.load('data/Play Rect.png'),
                         pos=(640, 300),
                         txt_inp='ИГРАТЬ', font=Font.new_font(75),
                         clr_base='#9933ff', clr_hvr='#ffffff')
            st_btn = Btn(
                img=pygame.image.load('data/test2.png'), pos=(640, 450),
                txt_inp='НАСТРОЙКИ',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#ffffff')
            qt_btn = Btn(img=pygame.image.load('data/test1.png'),
                         pos=(640, 600),
                         txt_inp='ВЫЙТИ', font=Font.new_font(75),
                         clr_base='#9933ff',
                         clr_hvr='#ffffff')

            for button in [pl_btn, st_btn, qt_btn]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pl_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()
                    if st_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        main_menu.options()
                    if qt_btn.checkForInput(menu_ms_pos):
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
            text_menu = Font.new_font(50).render('Выберите карту.', True,
                                                 '#6600ff')
            rect_menu = text_menu.get_rect(center=(660, 100))
            map1 = Btn(
                img=pygame.image.load('data/test1.png'), pos=(450, 250),
                txt_inp='Город',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            map2 = Btn(img=pygame.image.load('data/test1.png'),
                       pos=(850, 250),
                       txt_inp='Поле', font=Font.new_font(75),
                       clr_base='#9933ff',
                       clr_hvr='#8000ff')
            qt_btn = Btn(img=pygame.image.load('data/test4.png'),
                         pos=(640, 550),
                         txt_inp='МЕНЮ', font=Font.new_font(75),
                         clr_base='#9933ff',
                         clr_hvr='#8000ff')

            screen.blit(text_menu, rect_menu)
            for button in [map1, map2, qt_btn]:
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
                    if qt_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()

            pygame.display.update()

    def maps(mapp):
        while True:
            mapp = ''
            screen.blit(BG, (0, 0))
            menu_ms_pos = pygame.mouse.get_pos()
            text_menu = Font.new_font(50).render('Выберите карту.', True,
                                                 '#6600ff')
            rect_menu = text_menu.get_rect(center=(660, 100))
            map1 = Btn(
                img=pygame.image.load('data/test1.png'), pos=(450, 250),
                txt_inp='Город',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            map2 = Btn(img=pygame.image.load('data/test1.png'),
                       pos=(850, 250),
                       txt_inp='Поле', font=Font.new_font(75),
                       clr_base='#9933ff',
                       clr_hvr='#8000ff')
            qt_btn = Btn(img=pygame.image.load('data/test4.png'),
                         pos=(640, 550),
                         txt_inp='МЕНЮ', font=Font.new_font(75),
                         clr_base='#9933ff',
                         clr_hvr='#8000ff')

            screen.blit(text_menu, rect_menu)
            for button in [map1, map2, qt_btn]:
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
                    if qt_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.menu()

            pygame.display.update()

    def menu():
        while True:
            screen.blit(BG, (0, 0))
            screen.blit(logo, (330, 20))
            menu_ms_pos = pygame.mouse.get_pos()
            pl_btn = Btn(img=pygame.image.load('data/Play Rect.png'),
                         pos=(640, 250),
                         txt_inp='ИГРАТЬ', font=Font.new_font(75),
                         clr_base='#9933ff', clr_hvr='#8000ff')
            st_btn = Btn(
                img=pygame.image.load('data/test2.png'), pos=(640, 400),
                txt_inp='ПЕСОЧНИЦА',
                font=Font.new_font(75), clr_base='#9933ff', clr_hvr='#8000ff')
            qt_btn = Btn(img=pygame.image.load('data/test4.png'),
                         pos=(640, 550),
                         txt_inp='МЕНЮ', font=Font.new_font(75),
                         clr_base='#9933ff',
                         clr_hvr='#8000ff')

            for button in [pl_btn, st_btn, qt_btn]:
                button.changeColor(menu_ms_pos)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pl_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.maps('')
                    if st_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        play_menu.maps_sbox('')
                    if qt_btn.checkForInput(menu_ms_pos):
                        cnf_snd.play()
                        main_menu.main_menu()

            pygame.display.update()


main_menu.main_menu()
while pygame.mixer.music.get_busy():
    clock.tick(60)
    pygame.event.poll()
