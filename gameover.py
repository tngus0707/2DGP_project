from pico2d import *
open_canvas()
grass = load_image('gameover.jpg')

clear_canvas_now()
grass.draw_now(400, 300)
delay(5)
clear_canvas()
close_canvas()