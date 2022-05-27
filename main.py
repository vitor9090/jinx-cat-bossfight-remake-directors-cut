from ursina import *
from src.mo_entity import MoEntity
from src.client import Client
from src.boss import Boss

def main() -> None:
    app = Ursina(borderless=False)
    
    window.color = color.white

    camera.orthographic = True
    camera.fov = 16

    boss = Boss()
    client = Client()
    
    print('boss' in boss.mo_tags)
    
    app.run()

if __name__ == '__main__':
    main()

