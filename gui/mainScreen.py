import pygame
import gui.elements as elements

class MainScreen:

    def __init__(self, size, callbacks):
        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("CALX", (size[0] / 2, 60), 48, 1),
            elements.Text("The Personal Math Trainer", (size[0] / 2, 110), 26, 1),
            elements.Text("by @olivercrush (github)", (size[0] - 70, size[1] - 10), 16, 1),
            elements.Button("Commencer une session", (size[0] / 2, 230), (200, 50), callbacks[3]),
            elements.Button("Voir l'historique", (size[0] / 2, 290), (200, 50), None),
            elements.Button("Quitter", (size[0] / 2, 350), (200, 50), callbacks[0])
        ]

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen