import pygame
import gui.elements as elements

class SessionScreen:

    def __init__(self, size, callbacks):
        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("420", (size[0] / 2 + 60, 150), 50, 2),
            elements.Text("5356", (size[0] / 2 + 60, 190), 50, 2),
            elements.Text("+", (size[0] / 2 - 60, 190), 50, 0),
            elements.Rectangle((size[0] / 2, 230), (150, 2)),
        ]

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen