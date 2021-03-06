from pico2d import *
import enemy
import attack
import character
import Eattack

width, height = 800, 600
touch = False
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b + 50: return False
    if right_a < left_b - 50: return False
    if top_a < bottom_b - 50: return False
    if bottom_a > top_b + 50: return False

    return True

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
                attackClass.skill_pos = 0
            elif event.key == SDLK_l:
                attackClass.light_pos = 1
                attackClass.knife_pos = 0
                attackClass.skill_pos = 0
            elif event.key == SDLK_s:
                attackClass.skill_pos = 1
                attackClass.light_pos = 0
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

EattackClass = []
EattackClass.append(Eattack.EnemyAttack(350, 130, 'enemy1_attack'))
EattackClass.append(Eattack.EnemyAttack(350, 160, 'enemy1_attack'))
EattackClass.append(Eattack.EnemyAttack(350, 190, 'enemy1_attack'))

attackClass = attack.Attack(x, y)

characterClass = character.Character(x, y)

while running:
    delay(0.05)

    clear_canvas()
    cave.draw(width // 2, height // 2)
    for i in enemyClass:
        i.draw()
        i.update()
    for i in EattackClass:
        i.draw()
        i.update()

    door.draw(670, 320)

    # if characterClass.cnt == 5:
    #     dirY -= 5
    #     clear_canvas()
    #     import mainstate2
    #     close_canvas()

    if attackClass.UDLR == 0 or characterClass.UDLR == 0:
        if attackClass.knife_pos == 1:
            attackClass.draw()
            attackClass.update()

        if attackClass.light_pos == 1:
            attackClass.draw()
            attackClass.update()

            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        characterClass.draw()
        characterClass.update()
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        door.draw(670, 320)
        for i in enemyClass:
            i.draw()
            i.update()

        handle_events()


    if attackClass.UDLR == 1 or characterClass.UDLR == 1:
        attackClass.x += dirX
        characterClass.x += dirX
        x += dirX
        for e_attack in EattackClass:
            if collide(characterClass, e_attack):
                characterClass.hp -= 10
                characterClass.x -= 10

        for en in enemyClass:
            if collide(characterClass, en):
                characterClass.hp -= 10
                characterClass.x -= 10

        if attackClass.knife_pos == 1:
            attackClass.draw()
            attackClass.update()

            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1
            # for ea in EattackClass:
            #     if collide(attackClass, ea):
            #         EattackClass.remove(ea)

        if attackClass.light_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        if attackClass.skill_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

            # for en in enemyClass:
            #     if collide2(attackClass, en):
            #         enemyClass.remove(en)
            #         attackClass.draw2()

        characterClass.draw()
        characterClass.update()

        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        door.draw(670, 320)
        for i in enemyClass:
            i.draw()
            i.update()

        handle_events()

    if attackClass.UDLR == 2 or characterClass.UDLR == 2:
        characterClass.x += dirX
        attackClass.x += dirX
        x += dirX
        for e_attack in EattackClass:
            if collide(characterClass, e_attack):
                characterClass.hp -= 10
                characterClass.x += 10

        for en in enemyClass:
            if collide(characterClass, en):
                characterClass.hp -= 10
                characterClass.x += 10

        if attackClass.knife_pos == 1:
            attackClass.draw()
            attackClass.update()

            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1
            # for ea in EattackClass:
            #     if collide(attackClass, ea):
            #         EattackClass.remove(ea)

        if attackClass.light_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        if attackClass.skill_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        characterClass.draw()
        characterClass.update()
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        door.draw(670, 320)
        for i in enemyClass:
            i.draw()
            i.update()

        handle_events()

    if attackClass.UDLR == 3 or characterClass.UDLR == 3:
        characterClass.y += dirY
        attackClass.y += dirY
        y += dirY
        for e_attack in EattackClass:
            if collide(characterClass, e_attack):
                characterClass.hp -= 10
                characterClass.y += 10

        for en in enemyClass:
            if collide(characterClass, en):
                characterClass.hp -= 10
                characterClass.y -= 10

        if attackClass.knife_pos == 1:
            attackClass.draw()
            attackClass.update()

            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1
                    for ea in EattackClass:
                        EattackClass.remove(ea)
            # for ea in EattackClass:
            #     if collide(attackClass, ea):
            #         EattackClass.remove(ea)

        if attackClass.light_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        if attackClass.skill_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        characterClass.draw()
        characterClass.update()
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        door.draw(670, 320)
        for i in enemyClass:
            i.draw()
            i.update()

        handle_events()

    if attackClass.UDLR == 4 or characterClass.UDLR == 4:
        characterClass.y += dirY
        attackClass.y += dirY
        y += dirY
        for e_attack in EattackClass:
            if collide(characterClass, e_attack):
                characterClass.hp -= 10
                characterClass.y -= 10

        for en in enemyClass:
            if collide(characterClass, en):
                characterClass.hp -= 10
                characterClass.y += 10

        if attackClass.knife_pos == 1:
            attackClass.draw()
            attackClass.update()

            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1
                    for ea in EattackClass:
                        EattackClass.remove(ea)
            # for ea in EattackClass:
            #     if collide(attackClass, ea):
            #         EattackClass.remove(ea)



        if attackClass.light_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        if attackClass.skill_pos == 1:
            attackClass.draw()
            attackClass.update()
            for en in enemyClass:
                if collide(attackClass, en):
                    enemyClass.remove(en)
                    characterClass.point += 1
                    characterClass.cnt += 1

        characterClass.draw()
        characterClass.update()
        update_canvas()

        clear_canvas()
        cave.draw(width // 2, height // 2)
        door.draw(670, 320)

        for i in enemyClass:
            i.draw()
            i.update()

        handle_events()



handle_events()
close_canvas()