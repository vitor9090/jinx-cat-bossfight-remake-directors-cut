from random import randrange
import time

from ursina import *

# I can't believe i've coded something this bad lmao
# Please fix this shit
# My god
# Goofy ahh code

class FSText(Entity):
    def __init__(self, string: str, string_color, start_position):
        super().__init__()
        self.string = string
        self.text_position = start_position
        
        self.string_color = string_color
        
        self.direction = Vec2(0, 1)
        
        self.text = Text(text=self.string,
        position=self.position,
        color=self.string_color,
        origin=Vec2(0, 0),
        font='src/fonts/goofy_jinx.ttf'
        )
        
        self.force = -.02
        self.velocity = 0
        
        self.time_alive = 0
        self.max_time_alive = .5
        
    def update(self):
        if self.velocity == 0:
            self.velocity += .6
    
        self.velocity += self.force
        self.text.position += (self.direction * self.velocity * time.dt)
        
        if self.time_alive < self.max_time_alive:
            self.time_alive += time.dt
        else:
            destroy(self.text)
            destroy(self)
            
