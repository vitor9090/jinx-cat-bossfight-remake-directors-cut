from math import sin
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
                }
            ]
            
        self.current_phase = self.jinx_phases[0] 
        
        self.texture = self.current_phase['texture']
            
    def bounce(self, speed: float, multiplier: float) -> None:
        self.y = abs(sin(time.time() * speed)) * multiplier
            
    def update(self):
        super().update()
        
        self.current_phase['movement pattern'](10.0, 1.0)

