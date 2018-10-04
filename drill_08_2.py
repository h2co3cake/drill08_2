from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_line(p1, p2, p3):
    global x, y
    global LR

    if p1[0] < p2[0] :
        LR = 1

    elif p2[0] < p1[0]:
        LR = 0

        
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)
frame = 0
LR = 1
n = 1
size = 10
points = [(random.randint(0, KPU_WIDTH), random.randint(0, KPU_HEIGHT)) for i in range(size)]

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * LR, 100, 100, x, y)
    update_canvas()
    handle_events()

    p1 = points[n-2]
    p2 = points[n-1]
    p3 = points[n]

    n = (n + 1) % size

    draw_line(p1, p2, p3)

    frame = (frame + 1) % 8


    delay(0.05)

close_canvas()