import pygame
import gui.elements as elements

class MainScreen:

    def __init__(self, size, callbacks):
        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("CALX", (size[0] / 2, 30), 48),
            elements.Text("The Personal Math Trainer", (size[0] / 2, 80), 26),
            elements.Text("by @olivercrush (github)", (size[0] - 70, size[1] - 10), 16),
            elements.Button("Commencer une session", (size[0] / 2, 200), (200, 50), None),
            elements.Button("Voir l'historique", (size[0] / 2, 260), (200, 50), None),
            elements.Button("Quitter", (size[0] / 2, 320), (200, 50), callbacks[0])
        ]

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen