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

    def get_bb(self):
        if self.knife_pos == 1:
            if self.UDLR == 1:
                return self.x - 20 + 40, self.y - 20, self.x + 20 + 15, self.y + 20 - 30
            if self.UDLR == 2:
                return self.x - 20 - 20, self.y - 20 + 10, self.x + 20 - 50, self.y + 20 - 20
            if self.UDLR == 3:
                return self.x - 5, self.y - 20 + 40, self.x + 5, self.y + 20 + 15
            if self.UDLR == 4:
                return self.x - 20 + 15, self.y - 20 - 20, self.x + 20 - 10 , self.y + 20 - 50

        if self.light_pos == 1:
            if self.UDLR == 1:
                return self.x + 50 - 15, self. y - 10 - 15, self.x + 50 + 15, self.y - 10 + 15
            if self.UDLR == 2:
                return self.x - 50 - 15, self. y - 10 - 15, self.x - 50 + 15, self.y - 10 + 15
            if self.UDLR == 3:
                return self.x - 15, self. y + 50 - 15, self.x + 15, self.y + 50 + 15
            if self.UDLR == 4:
                return self.x - 15, self. y - 50 - 15, self.x + 15, self.y - 50 + 15


    def draw(self):
        if self.knife_pos == 1:
            if self.UDLR == 1:
                self.image.clip_draw(self.frame * 40, 0, 40, 40, self.x + 20, self.y)
            if self.UDLR == 2:
                self.image.clip_draw((self.frame + 1) * 40, 40, 40, 40, self.x - 30, self.y)
            if self.UDLR == 3:
                self.image.clip_draw((self.frame + 5) * 35, 160, 35, 32, self.x, self.y + 20)
            if self.UDLR == 4:
                self.image.clip_draw((self.frame + 1) * 40, 0, 40, 46, self.x - 5, self.y - 15)
        draw_rectangle(*self.get_bb())

        if self.light_pos == 1:
            if self.UDLR == 1:
                self.image2.clip_draw(self.frame * 50, 50, 50, 50, self.x + 50, self.y - 10)
            if self.UDLR == 2:
                self.image2.clip_draw(self.frame * 50, 50, 50, 50, self.x - 50, self.y - 10)
            if self.UDLR == 3:
                self.image2.clip_draw(self.frame * 50, 50, 50, 50, self.x, self.y + 50)
            if self.UDLR == 4:
                self.image2.clip_draw(self.frame * 50, 50, 50, 50, self.x, self.y - 50)

    def update(self):
        if self.knife_pos == 1:
            if self.UDLR == 0:
                self.frame = (self.frame + 1) % 2
            if self.UDLR == 1:
                self.frame = (self.frame + 1) % 2
            if self.UDLR == 2:
                self.frame = (self.frame + 1) % 2
            if self.UDLR == 3:
                self.frame = (self.frame + 5) % 2
            if self.UDLR == 4:
                self.frame = (self.frame + 3) % 2

        if self.light_pos == 1:
            if self.UDLR == 0:
                self.frame = (self.frame + 1) % 5
            if self.UDLR == 1 or self.UDLR == 2 or self.UDLR == 3 or self.UDLR == 4:
                self.frame = (self.frame + 1) % 5