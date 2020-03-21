import pygame
import gui.elements as elements

class MainScreen:

    def __init__(self, size):
        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("CALX", (size[0] / 2, 30), 48),
            elements.Text("The Personal Math Trainer", (size[0] / 2, 80), 26),
            elements.Text("by @olivercrush (github)", (size[0] - 70, size[1] - 10), 16),
            elements.Button("Bouton", (200, 200), (200, 150), None)
        ]

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen