from pico2d import *

class Character:
    def __init__(self, x, y):
        self.frame = 0
        self.x = x
        self.y = y
        self.UDLR = 0
        self.image = load_image('animation_sheet.png')

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw(self):
        if self.UDLR == 0:
            self.image.clip_draw(self.frame * 50, 350, 50, 50, self.x, self.y)
        if self.UDLR == 1:
            self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
        if self.UDLR == 2:
            self.image.clip_draw(self.frame * 50, 100, 50, 50, self.x, self.y)
        if self.UDLR == 3:
            self.image.clip_draw(self.frame * 50, 50, 50, 50, self.x, self.y)
        if self.UDLR == 4:
            self.image.clip_draw(self.frame * 50, 150, 50, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.UDLR == 0:
            self.frame = (self.frame + 1) % 3
        if self.UDLR == 1 or self.UDLR == 2 or self.UDLR == 3 or self.UDLR == 4:
            self.frame = (self.frame + 1) % 10
