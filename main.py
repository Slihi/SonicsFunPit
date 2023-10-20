import pyglet
from pyglet.window import key
from pyglet.gl import *


#Color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
tan = (210, 180, 140)

#Custom Window Class
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):

        #Window Variables
        minimum_width = 400
        minimum_height = 300
        default_width = 800
        default_height = 600
        caption = "Pyglet Window"
        resizable = True

        background_color = tan

        self.keys = set()

        super().__init__(width=default_width, height=default_height, caption=caption, resizable=resizable)
        
        #Set the minimum window size
        self.set_minimum_size(minimum_width, minimum_height)

        #Set the background color of the window
        glClearColor(background_color[0]/255, background_color[1]/255, background_color[2]/255, 1)



    def on_draw(self):
        self.clear()

    def on_resize(self, width, height):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)

    def on_key_release(self, symbol, modifiers):
        self.keys.remove(symbol)

    def update(self, dt):
        pass


#Main loop

if __name__ == "__main__":
    window = Window()
    pyglet.clock.schedule_interval(window.update, 1/60)
    pyglet.app.run()


