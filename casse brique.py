import core
import pygame
from pygame.math import Vector2
from block import Block

def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [600, 600]
    core.memory("c", Block())
    core.memory("listblock", [])
    core.memory("nbrblock", 30)
    for i in range(0, core.memory("nbrblock")):
        core.memory("listblock").append(Block())


def run ():
    core.cleanScreen()

    for monBlock in core.memory("listblock"):
        monBlock.show(core.screen)
















core.main(setup, run)