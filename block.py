import random
import pygame
from pygame.math import Vector2


class Block:
    def __init__(self):
        self.position = (10,10)
        self.longueur = 5
        self.largeur = 5
        self.rayon = 5
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 10


    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)



