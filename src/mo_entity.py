from ursina import *
from src.fstext import FSText


class MoEntity(Entity):
    def __init__(self, mo_tags=[]):
        super().__init__(
            model='quad'
            )
        self.mo_tags = mo_tags
        
        self.collider = 'box'
        
        self.health = 0
        self.max_health = 100
        
        self.damage_amount = 0
        
        self.hit_info = {'hit': False, 'actor': None, 'damage': 0}
        
        self.refresh_time = 0
        self.refresh_rate = .5
        
        self.textures_path = 'src/textures'
        
    def damage(self, amount: int, actor: str) -> None:
        self.health += amount
        
        FSText(str(self.health), color.red, self.position)
        
        self.hit_info['hit'] = True
        self.hit_info['actor'] = actor
        self.hit_info['damage'] = amount
        self.color = color.rgb(255, 0, 0)

    def update(self):
        if self.hit_info['hit']:
            self.refresh_time += time.dt
            if self.refresh_time > self.refresh_rate:
                    self.hit_info['hit'] = False
                    self.refresh_time = 0
                    self.color = color.rgb(255, 255, 255)
        
        if self.health > self.max_health:
            destroy(self)
