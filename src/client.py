from ursina import *
from src.mo_entity import MoEntity

class Client(MoEntity):
    def __init__(self, name='Name not found'):
        super().__init__(
                mo_tags=['player']
            )
        self.client_name = name
        
        self.visible = False
        
        self.scale=.5
        
        self.collider = 'box'
        
        self.max_health = 999
        
        self.damage_amount = 1
        
    def input(self, key):
        hit_info = self.intersects()
    
        if key == 'left mouse down':
            if MoEntity in type(hit_info.entity).__bases__:
                if 'boss' in hit_info.entity.mo_tags:
                    hit_info.entity.damage(self.damage_amount, self.client_name)
        
    def update(self):
        super().update()
        self.position = mouse.position * camera.fov
