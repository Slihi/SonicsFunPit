import pyglet
from pyglet.window import key
from pyglet.gl import *

#convention to define variables in all caps
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TAN = (210, 180, 140)

#Shader source code for pyglet'
#Vertex shader
vertex_source = """
#version 150 core
in vec2 position;
in vec4 colors;
out vec4 vertex_colors;

uniform mat4 projection;

void main()
{
    gl_Position = projection * vec4(position, 0.0, 1.0);
    vertex_colors = colors;
}
"""

#Fragment shader
fragment_source = """
#version 150 core
in vec4 vertex_colors;
out vec4 final_color;

void main()
{
    final_color = vertex_colors;
}
"""


#Custom Window Class
class Window(pyglet.window.Window):
    def __init__(self, minimum_size=(400, 300),
                 default_size=(800, 600)):

        self.window_size = default_size

        background_color = TAN

        self.keys = set()

        super().__init__(width=self.window_size[0],
                         height=self.window_size[1],
                         caption="Pyglet Window",
                         resizable=True)
        
        #Set the minimum window size
        self.set_minimum_size(minimum_size[0], minimum_size[1])

        #Set the background color of the window
        glClearColor(background_color[0]/255, background_color[1]/255, background_color[2]/255, 1)

    def on_draw(self):
        self.clear()

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)

        # Remove if better close method is implemented
        if key.ESCAPE in self.keys:
            self.close()

    def on_key_release(self, symbol, modifiers):
        self.keys.remove(symbol)

    def update(self, dt):
        pass

if __name__ == "__main__":
    window = Window()
    pyglet.clock.schedule_interval(window.update, 1/60)
    pyglet.app.run()


