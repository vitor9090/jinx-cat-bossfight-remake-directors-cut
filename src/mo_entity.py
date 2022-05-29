from ursina import *
from src.fstext import FSText


class MoEntity(Entity):
    def __init__(self, mo_tags=[]):
        super().__init__(
            model='quad'
            )
        self.mo_tags = mo_tags
        
        self.src_path = 'src/'
        
        self.collider = 'box'
        
        self.hit_sound = Audio(
        f'{self.src_path}sounds/snd_attack_hit.wav',
        autoplay=False,
        volume=.3,
        )
        
        self.health = 0
        self.max_health = 100
        
        self.states = {
            'alive': 0,
            'dead': 1
        }
        
        self.state = self.states['alive']
        
        self.damage_amount = 0
        
        self.hit_info = {'hit': False, 'actor': None, 'damage': 0}
        
        self.refresh_time = 0
        self.refresh_rate = .5
        
    def damage(self, amount: int, actor: str) -> None:
        if self.state == self.states['alive']:
            self.health += amount
                        
            self.hit_info['hit'] = True
            self.hit_info['actor'] = actor
            self.hit_info['damage'] = amount
            self.color = color.rgb(255, 0, 0)
            
            FSText(str(self.hit_info['damage']), color.red, self.position / camera.fov)
            
            self.hit_sound.play()

    def update(self):
        if self.state == self.states['alive']:
            if self.hit_info['hit']:
                self.refresh_time += time.dt
                if self.refresh_time > self.refresh_rate:
                        self.hit_info['hit'] = False
                        self.refresh_time = 0
                        self.color = color.rgb(255, 255, 255)
            
            if self.health > self.max_health:
                self.state = self.states['dead']
