"""
The Model class: This defines the business logic or operations attached to certain
tasks from the client.
"""
import pygame
pygame.font.init()


class Model(object):
    def __init__(self):
        self.myfont = pygame.font.SysFont('Areal', 30)
        self.textsurface = ""
        self.width = 620
        self.height = 480
        self.display = pygame.display.set_caption('Card Game!')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.red = 0
        self.green = 0
        self.blue = 0

    def get_screen(self):
        return self.screen

    def make_color(self, red, green, blue):
        color = (red, green, blue)
        return color

    def get_font(self):
        return self.font

    def set_font_size(self, size):
        self.font_size = size

    def make_text(self, message, size):
        font = pygame.font.SysFont("comicsansms", size)
        text = font.render(message, True, (0, 0, 0))
        return text
