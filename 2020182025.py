from pico2d import *

width, height = 800, 600

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
                UDLR = 0
            elif event.key == SDLK_LEFT:
                dirX -= 5
                UDLR = 1
            elif event.key == SDLK_UP:
                dirY += 5
                UDLR = 2
            elif event.key == SDLK_DOWN:
                dirY -= 5
                UDLR = 3
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
knife = load_image('knife.png')
knifeUP = load_image('knife_up.png')
knifeDOWN = load_image('knife_down.png')
attack = load_image('attack.png')

running = True
UDLR = 0
knife_pos = 0
attack_pos = 0

x = 800 // 2
y = 600 // 2

frame = 0
enemy1_frame = 0
knife_frame = 0
knifeUP_frame = 0
knifeDOWN_frame = 0
attack_frame = 0
dirX = 0
dirY = 0

while running:
    clear_canvas()
    cave.draw(width // 2, height // 2)
    enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 200, 400)

    if UDLR == 0:

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

        frame = (frame + 1) % 10
        x += dirX
        delay(0.03)

        handle_events()

    if UDLR == 1:
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

        frame = (frame + 1) % 10
        x += dirX
        delay(0.03)



    handle_events()

    if UDLR == 2:

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

        frame = (frame + 1) % 10
        y += dirY
        delay(0.03)

        handle_events()

    if UDLR == 3:
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

        frame = (frame + 1) % 10
        y += dirY
        delay(0.03)

        handle_events()

    handle_events()

close_canvas()