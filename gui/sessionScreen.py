import pygame
import gui.elements as elements

class SessionScreen:

    def __init__(self, size, callbacks):
        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("   42", (size[0] / 2, 150), 50),
            elements.Text("   53", (size[0] / 2, 200), 50),
            elements.Text("+", (size[0] / 2 - 50, 195), 50),
        ]

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen