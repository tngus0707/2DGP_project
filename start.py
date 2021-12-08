from pico2d import *
open_canvas()
grass = load_image('start.jpeg')

clear_canvas_now()
grass.draw_now(400, 300)
delay(2)
events = get_events()
import mainstate1

