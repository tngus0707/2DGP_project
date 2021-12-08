from pico2d import *

class Enemy:
    def __init__(self, x, y, type):
        self.frame = 0
        self.x = x
        self.y = y
        self.dead = 0

        if type == 'enemy1':
            self.image = load_image('enemy1.png')
            self.image2 = load_image('enemy1.png')
            self.sizeX = 30
            self.sizeY = 30
            self.bottom = 170
            self.enemyX = 320
            self.enemyY = 130
            self.frame_count = 4

        if type == 'enemy2':
            self.image = load_image('enemy2.png')
            self.image2 = load_image('enemy2.png')
            self.sizeX = 40
            self.sizeY = 40
            self.bottom = 210
            self.enemyX = 150
            self.enemyY = 230
            self.frame_count = 4

        if type == 'enemy3':
            self.image = load_image('enemy3.png')
            self.image2 = load_image('enemy3.png')
            self.sizeX = 33
            self.sizeY = 40
            self.bottom = 40
            self.enemyX = 180
            self.enemyY = 480
            self.frame_count = 3

    def get_bb(self):
        return self.x - self.sizeX / 2, self.y - self.sizeY / 2, self.x + self.sizeX / 2, self.y + self.sizeY / 2

    def draw(self):
        self.image.clip_draw(self.frame * self.sizeX, self.bottom, self.sizeX, self.sizeY, self.x, self.y)
        draw_rectangle(*self.get_bb())

    # def draw2(self):
    #     self.image2.clip_draw(self.frame * self.sizeX, self.bottom, self.sizeX, self.sizeY, self.x, self.y)
    #     draw_rectangle(*self.get_bb())

    def update(self):
        self.frame = (self.frame + 1) % self.frame_count
