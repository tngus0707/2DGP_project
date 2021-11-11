from pico2d import *

width, height = 800, 600

#character Event
UP_DOWN, DOWN_DOWN, RIGHT_DOWN, LEFT_DOWN, UP_UP, DOWN_UP, RIGHT_UP, LEFT_UP = range(8)

key_event_Table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,

    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
}

def handle_events():
    global running
    global dirX
    global dirY
    global UDLR
    global knife_pos
    global attack_pos

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 5
                UDLR = 1
            elif event.key == SDLK_LEFT:
                dirX -= 5
                UDLR = 2
            elif event.key == SDLK_UP:
                dirY += 5
                UDLR = 3
            elif event.key == SDLK_DOWN:
                dirY -= 5
                UDLR = 4
            elif event.key == SDLK_k:
                knife_pos = 1
                attack_pos = 0
            elif event.key == SDLK_l:
                attack_pos = 1
                knife_pos = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 5
            elif event.key == SDLK_LEFT:
                dirX += 5
            elif event.key == SDLK_UP:
                dirY -= 5
            elif event.key == SDLK_DOWN:
                dirY += 5

    pass

open_canvas(width, height)

cave = load_image('cave.png')
character = load_image('animation_sheet.png')
enemy1 = load_image('enemy1.png')
enemy2 = load_image('enemy2.png')
enemy3 = load_image('enemy3.png')
knife = load_image('knife.png')
knifeUP = load_image('knife_up.png')
knifeDOWN = load_image('knife_down.png')
attack = load_image('attack.png')
door = load_image('door.png')

running = True
UDLR = 0
knife_pos = 0
attack_pos = 0

x = 670
y = 320

frame = 0
enemy1_frame = 0
enemy2_frame = 0
enemy3_frame = 0
knife_frame = 0
knifeUP_frame = 0
knifeDOWN_frame = 0
attack_frame = 0
dirX = 0
dirY = 0

while running:
    clear_canvas()
    cave.draw(width // 2, height // 2)
    enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
    enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
    enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
    enemy1_frame = (enemy1_frame + 1) % 4
    delay(0.03)


    enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
    enemy2_frame = (enemy2_frame + 1) % 4
    delay(0.03)


    enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
    enemy3_frame = (enemy3_frame + 1) % 3
    door.draw(670, 320)

    if UDLR == 0:
        if knife_pos == 1:
            knife.clip_draw(knife_frame * 40, 0, 40, 40, x + 20, y)
            update_canvas()

        if attack_pos == 1:
            attack.clip_draw(attack_frame * 50, 0, 50, 50, x + 50, y - 10)
            update_canvas()

        character.clip_draw(frame * 50, 350, 50, 50, x, y) #left, bottom, width, height, x, y
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        character.clip_draw(frame * 50, 350, 50, 50, x, y)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 3
        delay(0.1)

        handle_events()

    if UDLR == 1:

        if knife_pos == 1:
            knife.clip_draw(knife_frame * 40, 0, 40, 40, x + 20, y)
            update_canvas()

        if attack_pos == 1:
            attack.clip_draw(attack_frame * 50, 0, 50, 50, x + 50, y - 10)
            update_canvas()

        character.clip_draw(frame * 50, 0, 50, 50, x, y) #left, bottom, width, height, x, y
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 10
        x += dirX
        delay(0.01)

        handle_events()

    if UDLR == 2:
        if knife_pos == 1:
            knife.clip_draw(knife_frame * 40, 40, 40, 40, x - 30, y)
            update_canvas()

        if attack_pos == 1:
            attack.clip_draw(attack_frame * 50, 0, 50, 50, x - 50, y - 10)
            update_canvas()

        character.clip_draw(frame * 50, 100, 50, 50, x, y)
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 10
        x += dirX
        delay(0.01)

        handle_events()

    if UDLR == 3:

        if knife_pos == 1:
            knifeUP.clip_draw(knifeUP_frame * 38, 0, 38, 32, x, y + 40)
            update_canvas()

        if attack_pos == 1:
            attack.clip_draw(attack_frame * 50, 0, 50, 50, x, y + 50)
            update_canvas()

        character.clip_draw(frame * 50, 50, 50, 50, x, y)
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 10
        y += dirY
        delay(0.01)

        handle_events()

    if UDLR == 4:

        if knife_pos == 1:
            knifeDOWN.clip_draw(knifeDOWN_frame * 40, 0, 40, 46, x, y - 40)
            update_canvas()

        if attack_pos == 1:
            attack.clip_draw(attack_frame * 50, 0, 50, 50, x, y - 50)
            update_canvas()

        character.clip_draw(frame * 50, 150, 50, 50, x, y)
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 10
        y += dirY
        delay(0.01)

        handle_events()

handle_events()

close_canvas()