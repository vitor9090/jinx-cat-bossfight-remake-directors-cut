from random import choice
import time

from ursina import *

class FSText(Entity):
    def __init__(self, string: str, string_color, start_position):
        super().__init__()
        self.string = string
        self.text_position = start_position
        
        self.string_color = string_color
        
        self.direction = Vec2(choice([-1, 0, 1]), choice([-1, 0, 1]))
        
        self.text = Text(text=self.string,
        position=self.position,
        color=self.string_color,
        origin=Vec2(0, 0),
        font='src/fonts/goofy_jinx.ttf'
        )
        
        self.speed = 0.2
        
        self.time_alive = 0
        self.max_time_alive = 2
        
    def update(self):
        self.text.position += (self.direction * self.speed * time.dt)
        self.speed -= .002
        
        if self.time_alive < self.max_time_alive:
            self.time_alive += time.dt
        else:
            destroy(self.text)
            destroy(self)
            
