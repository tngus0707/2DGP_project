from pico2d import *

class Attack:
    def __init__(self, x, y):
        self.frame = 0
        self.x = x
        self.y = y
        self.UDLR = 0
        self.knife_pos = 0
        self.light_pos = 0
        self.image = load_image('knife.png')
        self.image2 = load_image('attack.png')

    def draw(self):
        if self.knife_pos == 1:
            if self.UDLR == 1:
                self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x + 20, self.y)
            if self.UDLR == 2:
                self.image.clip_draw(self.frame * 40, 40, 40, 40, self.x - 30, self.y)
            if self.UDLR == 3:
                self.image.clip_draw(self.frame * 38, 0, 38, 32, self.x, self.y + 40)
            if self.UDLR == 4:
                self.image.clip_draw(self.frame * 40, 0, 40, 46, self.x, self.y - 40)

        if self.light_pos == 1:
            if self.UDLR == 1:
                self.image2.clip_draw(self.frame * 50, 0, 50, 50, self.x + 50, self.y - 10)
            if self.UDLR == 2:
                self.image2.clip_draw(self.frame * 50, 0, 50, 50, self.x - 50, self.y - 10)
            if self.UDLR == 3:
                self.image2.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y + 50)
            if self.UDLR == 4:
                self.image2.clip_draw(self.frame * 50, 0, 50, 50, self.x - 50, self.y - 10)

    def update(self):
        delay(0.03)