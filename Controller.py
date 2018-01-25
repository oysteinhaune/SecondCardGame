from Model import Model
from View import View

"""
The Controller class: This is essentially an interface that is between the view and
model. When the client takes certain actions, the controller directs the query from the
view to model.
"""

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.velkommen_text = ''

    def intro_screen(self):
        color = self.model.make_color(255, 255, 255)
        screen = self.model.get_screen()
        self.view.fill(color, screen)

        text = self.model.make_text('Velkommen til Card Game!', 40)
        text2 = self.model.make_text('Trykk enter for å starte', 20)
        self.view.update(text, 60, 50, screen)
        self.view.update(text2, 200, 200, screen)
        self.view.flip()

