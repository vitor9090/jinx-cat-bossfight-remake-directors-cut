from math import sin, cos, sqrt, pi, asin

import time

from ursina import *

from src.mo_entity import MoEntity

#listen to EDEN on spotify! it's really good.

class Boss(MoEntity):
    def __init__(self):
        super().__init__(
                mo_tags=['boss']
            )
            
        self.scale = 2
        
        self.jinx_phases = [
                {
                'texture': Texture(f'{self.src_path}/textures/jinx_my_beloved.jpg'),
                'movement pattern': self.bounce
                },
                {
                'texture': Texture(f'{self.src_path}/textures/jinx_phase_1.jpg'),
                'movement pattern': self.hourglass
                }
            ]
            
        
        self.health = 0
        self.max_health = 200
        
        self.phase_num = 0
            
    def bounce(self) -> None:
        self.x = 0
        self.y = abs(sin(time.time() * 10)) * 2
        
    def hourglass(self) -> None:
        self.x = (cos(time.time() * 2) * 2)
        self.y = (sin(time.time() * 2) * 2) * pi/self.x
        
    def input(self, key):
        if key == '.':
            self.phase_num += 1
            self.phase_num %= len(self.jinx_phases)
        if key == ',':
            self.phase_num -= 1
            self.phase_num %= len(self.jinx_phases)

        
    def update(self):
        super().update()
        if self.health > 100:
            self.phase_num = 1
        else:
            self.phase_num = 0

        self.jinx_phases[self.phase_num]['movement pattern']()
        self.texture = self.jinx_phases[self.phase_num]['texture']

