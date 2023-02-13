from sandbox import*
from main_board import MainBoard
from AnimSpites import Font


class Game:
    def main(mapp):
        pygame.init()
        sht_snd = pygame.mixer.Sound('data/vystrel-tanka.mp3')
        pygame.display.set_caption('Игра')
        size = width, height = 1920 * 3 / 4, 1080 * 3 / 4
        screen = pygame.display.set_mode(size)
        board = MainBoard(11, 11, 100, 10, 70, mapp)
        board.set_view(300, 10, 70)
        board.first_render(screen)
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        running = True
        time_on = False
        speed = 15
        ticks = 0
        last_chosen = None
        default_mc = 3 # кол-во ходов по условию
        move_counter = default_mc
        board.player = 0
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    board.dest = 0, 0
                    board.rot = 0
                    board.get_click(event.pos)
                if board.chosen:
                    if event.type == pygame.KEYDOWN and board.focused_cell:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            board.dest = 0, -1
                            move_counter -= 1
                            board.rot = 0
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            board.dest = 0, 1
                            move_counter -= 1
                            board.rot = 0
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            board.dest = 0, 0
                            board.rot = 90
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            board.dest = 0, 0
                            board.rot = -90
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            move_counter -= 1
                            sht_snd.play()
                            board.shoot()
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            os.system('python backtomenu.py')
            if move_counter == 0:
                if board.bullet_ex == 0:
                    board.player = (board.player + 1) % 2
                    move_counter = default_mc
                    board.chosen = 0
                    board.focused.kill()
                    if last_chosen:
                        tmp_chosen = last_chosen
                        last_chosen = board.focused_cell
                        board.on_click(tmp_chosen)
                    else:
                        last_chosen = board.focused_cell

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, "#d55800", (
                board.left, board.top, board.cell_size * board.width, board.cell_size * board.height))  # подложка
            board.first_render(screen)
            board.map_sp.draw(screen)  # создание карты
            board.render(screen)
            board.extra_sp.draw(screen)
            clr = ''
            if move_counter == 1:
                clr = '#ff0000'
            else:
                clr = '#ffffff'
            MV_TEXT = Font.new_font(12).render(
                f'Кол-во оставшихся ходов: {move_counter}', True,
                clr)
            MV_RECT = MV_TEXT.get_rect(center=(130, 100))
            screen.blit(MV_TEXT, MV_RECT)
            color = ''
            if board.player == 0:
                color = 'Зелёные'
                clr = '#008000'
            elif board.player == 1:
                color = 'Красные'
                clr = '#ff0000'
            ST_TEXT = Font.new_font(12).render(
                f'Текущая сторона: {color}', True,
                clr)
            ST_RECT = ST_TEXT.get_rect(center=(130, 140))
            screen.blit(ST_TEXT, ST_RECT)
            if move_counter == 0:
                board.player = (board.player + 1) % 2
                move_counter = default_mc
                board.chosen = 0
                board.focused.kill()
                if last_chosen:
                    tmp_chosen = last_chosen
                    last_chosen = board.focused_cell
                    board.on_click(tmp_chosen)
                else:
                    last_chosen = board.focused_cell
            board.endgame()
            if ticks >= speed:
                if time_on:
                    board.next_move()
                ticks = 0
            pygame.display.flip()
            clock.tick(60)
            ticks += 1
        pygame.quit()


if __name__ == "__main__":
    all_sprites = pygame.sprite.Group()
    Game.main() #выбор, что запускать, песочницу или игру main/sandbox