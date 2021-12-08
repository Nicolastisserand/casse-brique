import random
import pygame
from pygame.math import Vector2

class balle:
    def __init__(self):
        self.position = Vector2(300,300)
        self.rayon = 10
        self.couleur = (255,255,255)


    def show(self,screen):
        pygame.draw.circle(screen,self.couleur,self.position,self.rayon)