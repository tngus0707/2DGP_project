from pico2d import *

width, height = 800, 600

open_canvas(width, height)

cave = load_image('cave.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                LR = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                LR = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



running = True
LR = 1
x = 800 // 2
frame = 0
dir = 0

while running:
    clear_canvas()
    cave.draw(width // 2, height // 2)

    if LR == 1:

        character.clip_draw(frame * 50, 0, 50, 50, x, 90) #left, bottom, width, height, x, y
        update_canvas()
        clear_canvas()
        cave.draw(width // 2, height // 2)

        handle_events()

        frame = (frame + 1) % 10
        x += dir * 5
        delay(0.03)

    if LR == 0:

        character.clip_draw(frame * 50, 100, 50, 50, x, 90)
        update_canvas()
        clear_canvas()
        cave.draw(width // 2, height // 2)

        handle_events()

        frame = (frame + 1) % 10
        x += dir * 5
        delay(0.03)

close_canvas()