class Btn():
    def __init__(self, img, pos, txt_inp, font, clr_base,
                 clr_hvr):
        self.img = img
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.clr_base, self.clr_hvr = clr_base, clr_hvr
        self.txt_inp = txt_inp
        self.txt = self.font.render(self.txt_inp, True, self.clr_base)
        if self.img is None:
            self.img = self.txt
        self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))
        self.txt_rect = self.txt.get_rect(center=(self.x_pos, self.y_pos))

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1] in range(
                self.rect.top, self.rect.bottom):
            return True
        return False

    def update(self, screen):
        if self.img is not None:
            screen.blit(self.img, self.rect)
        screen.blit(self.txt, self.txt_rect)

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1] in range(
                self.rect.top, self.rect.bottom):
            self.txt = self.font.render(self.txt_inp, True,
                                         self.clr_hvr)
        else:
            self.txt = self.font.render(self.txt_inp, True,
                                         self.clr_base)
