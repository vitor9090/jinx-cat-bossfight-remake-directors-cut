from math import sin
import time
from ursina import *
from src.mo_entity import MoEntity

class Boss(MoEntity):
    def __init__(self):
        super().__init__(
                mo_tags=['boss']
            )
            
        self.scale = 2
            
        jinx_phases_textures = [Texture(f'{self.textures_path}/jinx_my_beloved.jpg')]
        
        self.texture = jinx_phases_textures[0]
            
            
    def bounce(self, speed: float, multiplier: float) -> float:
        return abs(sin(time.time() * speed)) * multiplier
            
    def update(self):
        super().update()
        
        self.y = self.bounce(10.0, 3.0)
