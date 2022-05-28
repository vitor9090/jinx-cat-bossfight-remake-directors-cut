from ursina import *

from src.mo_entity import MoEntity
from src.fstext import FSText

from src.client import Client
from src.boss import Boss

def main() -> None:
    app = Ursina(borderless=False)
    
    window.color = color.white

    camera.orthographic = True
    camera.fov = 16

    boss = Boss()
    client = Client()
    
    #FSText('FSText text', color.red, boss.position * camera.fov)
    
    app.run()

if __name__ == '__main__':
    main()

