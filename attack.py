from pico2d import *

class Attack:
    def __init__(self, x, y, type):
        self.frame = 0
        self.x = x
        self.y = y

        if type == 'knifeR':
            self.image = load_image('knife.png')
            self.sizeX = 40
            self.sizeY = 40
            self.bottom = 0

        if type == 'knifeL':
            self.image = load_image('knife.png')
            self.sizeX = 40
            self.sizeY = 40
            self.bottom = 40

        if type == 'knifeUP':
            self.image = load_image('knife.png')
            self.sizeX = 38
            self.sizeY = 32
            self.bottom = 0

        if type == 'knifeDOWN':
            self.image = load_image('knife.png')
            self.sizeX = 40
            self.sizeY = 46
            self.bottom = 0

        if type == 'lightR':
            self.image = load_image('attack.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0

        if type == 'lightL':
            self.image = load_image('attack.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0

        if type == 'lightUP':
            self.image = load_image('attack.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0

        if type == 'lightDOWN':
            self.image = load_image('attack.png')
            self.sizeX = 50
            self.sizeY = 50
            self.bottom = 0

    def draw(self):
        self.image.clip_draw(self.frame * self.sizeX, self.bottom, self.sizeX, self.sizeY, self.x, self.y)

    # def update(self):
    #     self.frame = (self.frame + 1) & self.frame_count
    #     delay(0.03)