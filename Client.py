import sys

from Controller import Controller
import pygame


class Client(object):
    def __init__(self):
        pygame.init()
        self.controller = Controller()
        self.gameloop = True
        self.clock = pygame.time.Clock()
        self.game_fps = 60
        self.start_gameloop()

    def start_gameloop(self):
        screen = "intro"
        while self.gameloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if screen == "intro":
                self.controller.intro_screen()
                screen = "waiting"
            self.clock.tick(self.game_fps)


NewGame = Client()
