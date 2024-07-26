import pygame
from pygame.math import Vector2


class Cell:
    def __init__(self, pos):
        self.alive = False
        self.pos = pos
        self.color = "white"
        self.neighbors = []

    def set_color(self):
        if self.alive:
            self.color = "black"
        else:
            self.color = "white"

    def kill(self):
        self.alive = False
        self.set_color()

    def revive(self):
        self.alive = True
        self.set_color()

    def draw(self, screen, size):
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.pos.x * size,
                self.pos.y * size,
                size,
                size,
            ),
        )
