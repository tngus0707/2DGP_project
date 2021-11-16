from pico2d import *
import enemy
import attack
import character

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
                attackClass.UDLR = 1
                characterClass.UDLR = 1
            elif event.key == SDLK_LEFT:
                dirX -= 5
                attackClass.UDLR = 2
                characterClass.UDLR = 2
            elif event.key == SDLK_UP:
                dirY += 5
                attackClass.UDLR = 3
                characterClass.UDLR = 3
            elif event.key == SDLK_DOWN:
                dirY -= 5
                attackClass.UDLR = 4
                characterClass.UDLR = 4
            elif event.key == SDLK_k:
                attackClass.knife_pos = 1
                attackClass.light_pos = 0
            elif event.key == SDLK_l:
                attackClass.light_pos = 1
                attackClass.knife_pos = 0
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
characters = load_image('animation_sheet.png')
enemy1 = load_image('enemy1.png')
enemy2 = load_image('enemy2.png')
enemy3 = load_image('enemy3.png')
knife = load_image('knife.png')
light = load_image('attack.png')
knifeUP = load_image('knife_up.png')
knifeDOWN = load_image('knife_down.png')
door = load_image('door.png')

running = True

x = 670
y = 320

frame = 0
enemy1_frame = 0
enemy2_frame = 0
enemy3_frame = 0
knife_frame = 0
knifeUP_frame = 0
knifeDOWN_frame = 0
light_frame = 0
dirX = 0
dirY = 0

enemyClass = []
enemyClass.append(enemy.Enemy(320, 130, 'enemy1'))
enemyClass.append(enemy.Enemy(320, 160, 'enemy1'))
enemyClass.append(enemy.Enemy(320, 190, 'enemy1'))
enemyClass.append(enemy.Enemy(150, 230, 'enemy2'))
enemyClass.append(enemy.Enemy(180, 480, 'enemy3'))

attackClass = attack.Attack(x, y)

characterClass = character.Character(x, y)

while running:
    clear_canvas()
    cave.draw(width // 2, height // 2)
    for i in enemyClass:
        i.draw()
        i.update()

    door.draw(670, 320)

    if attackClass.UDLR == 0 or characterClass.UDLR == 0:
        if attackClass.knife_pos == 1:
            attackClass.draw()

        if attackClass.light_pos == 1:
            attackClass.draw()

        characterClass.draw()
        characterClass.update()
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        characters.clip_draw(frame * 50, 350, 50, 50, x, y)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 130)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 160)
        enemy1.clip_draw(enemy1_frame * 30, 170, 30, 30, 320, 190)
        enemy2.clip_draw(enemy2_frame * 40, 210, 40, 40, 150, 230)
        enemy3.clip_draw(enemy3_frame * 33, 40, 33, 40, 180, 480)
        door.draw(670, 320)

        frame = (frame + 1) % 3
        delay(0.1)

        handle_events()

    if attackClass.UDLR == 1 or characterClass.UDLR == 1:
        attackClass.x += dirX
        characterClass.x += dirX
        x += dirX
        if attackClass.knife_pos == 1:
            attackClass.draw()

        if attackClass.light_pos == 1:
            attackClass.draw()

        characterClass.draw()
        characterClass.update()

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
        delay(0.01)

        handle_events()

    if attackClass.UDLR == 2 or characterClass.UDLR == 2:
        characterClass.x += dirX
        attackClass.x += dirX
        x += dirX
        if attackClass.knife_pos == 1:
            attackClass.draw()

        if attackClass.light_pos == 1:
            light.clip_draw(light_frame * 50, 0, 50, 50, x - 50, y - 10)
            update_canvas()

        characterClass.draw()
        characterClass.update()
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
        delay(0.01)

        handle_events()

    if attackClass.UDLR == 3 or characterClass.UDLR == 3:
        characterClass.y += dirY
        attackClass.y += dirY
        y += dirY

        if attackClass.knife_pos == 1:
            attackClass.draw()

        if attackClass.light_pos == 1:
            light.clip_draw(light_frame * 50, 0, 50, 50, x, y + 50)
            update_canvas()

        characterClass.draw()
        characterClass.update()
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
        delay(0.01)

        handle_events()

    if attackClass.UDLR == 4 or characterClass.UDLR == 4:
        characterClass.y += dirY
        attackClass.y += dirY
        y += dirY

        if attackClass.knife_pos == 1:
            attackClass.draw()

        if attackClass.light_pos == 1:
            light.clip_draw(light_frame * 50, 0, 50, 50, x, y - 50)
            update_canvas()

        characterClass.draw()
        characterClass.update()
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
        delay(0.01)

        handle_events()

handle_events()

close_canvas()