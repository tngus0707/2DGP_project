from pico2d import *

class Character:
    def __init__(self, x, y):
        self.frame = 0
        self.x = x
        self.y = y
        self.UDLR = 0
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.point = 0
        self.cnt = 0
        self.hp = 100

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def draw(self):
        if self.UDLR == 0:
            self.image.clip_draw(self.frame * 50, 350, 50, 50, self.x, self.y)
        if self.UDLR == 1:
            if self.hp <= 0:
                import gameover

            self.image.clip_draw(self.frame * 50, 0, 50, 50, self.x, self.y)
        if self.UDLR == 2:
            if self.hp <= 0:
                import gameover

            self.image.clip_draw(self.frame * 50, 100, 50, 50, self.x, self.y)
        if self.UDLR == 3:
            if self.hp <= 0:
                import gameover

            self.image.clip_draw(self.frame * 50, 50, 50, 50, self.x, self.y)
        if self.UDLR == 4:
            if self.hp <= 0:
                import gameover

            self.image.clip_draw(self.frame * 50, 150, 50, 50, self.x, self.y)
        self.font.draw(self.x - 30, self.y + 30, 'score : ' + str(self.point), (255, 255, 0))
        # self.font.draw(self.x - 30, self.y + 50, 'cnt : ' + str(self.cnt), (0, 255, 0))
        self.font.draw(self.x - 30, self.y + 50, 'HP : ' + str(self.hp), (0, 0, 255))



        # draw_rectangle(*self.get_bb())

    def update(self):
        if self.UDLR == 0:
            self.frame = (self.frame + 1) % 3
        if self.UDLR == 1 or self.UDLR == 2 or self.UDLR == 3 or self.UDLR == 4:
            self.frame = (self.frame + 1) % 10
