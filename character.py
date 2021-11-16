from pico2d import *

class Character:
    def __init__(self, x, y, type):
        self.frame = 0
        self.x = x
        self.y = y

        if type == 'characterR':
            self.image = load_image('animation_sheet.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0
            self.characterX = x
            self.characterY = y
            self.frame_count = 10

        if type == 'characterL':
            self.image = load_image('animation_sheet.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 100
            self.characterX = x
            self.characterY = y
            self.frame_count = 10

        if type == 'characterUP':
            self.image = load_image('animation_sheet.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0
            self.characterX = x
            self.characterY = y
            self.frame_count = 10

        if type == 'characterL':
            self.image = load_image('animation_sheet.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 150
            self.characterX = x
            self.characterY = y
            self.frame_count = 10

    def draw(self):
        self.image.clip_draw(self.frame * self.sizeX, self.bottom, self.sizeX, self.sizeY, self.characterX, self.characterY)

    def update(self):
        self.frame = (self.frame + 1) & self.frame_count
        delay(0.03)