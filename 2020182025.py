from pico2d import *

width, height = 800, 600



def handle_events():
    global running
    global dirX
    global dirY
    global UDLR

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

running = True
UDLR = 0
x = 800 // 2
y = 600 // 2
frame = 0
dirX = 0
dirY = 0

while running:
    clear_canvas()
    cave.draw(width // 2, height // 2)

    if UDLR == 0:

        character.clip_draw(frame * 50, 0, 50, 50, x, y) #left, bottom, width, height, x, y
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)

        frame = (frame + 1) % 10
        x += dirX
        delay(0.03)

        handle_events()

    if UDLR == 1:

        character.clip_draw(frame * 50, 100, 50, 50, x, y)
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)

        frame = (frame + 1) % 10
        x += dirX
        delay(0.03)

        handle_events()

    if UDLR == 2:

        character.clip_draw(frame * 50, 50, 50, 50, x, y)
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)

        frame = (frame + 1) % 10
        y += dirY
        delay(0.03)

        handle_events()

    if UDLR == 3:
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