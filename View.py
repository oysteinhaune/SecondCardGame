"""
The View class: This defines the view or representation that is viewed by the client.
The model presents the data to the view based on the business logic.
"""
import pygame
from Model import Model


class View(object):

    def fill(self, color, screen):
        screen.fill(color)

    def update(self, data, posx, posy, screen):
        screen.blit(data, (posx, posy))
        print("updating")

    def flip(self):
        pygame.display.flip()
