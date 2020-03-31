import pygame
import gui.elements as elements
import time

COUNTEVENT = pygame.USEREVENT+1
t = 1000

class WaitingScreen:

    def __init__(self, size, callbacks, count):
        self.count = count
        self.callbacks = callbacks

        self.background = (245, 245, 245)
        self.elements = [
            elements.Text(str(count), (size[0] / 2, 170), 50, 1),
            elements.Button("Annuler", (size[0] / 2, 250), (200, 50), self.callbacks[1]),
        ]

        pygame.time.set_timer(COUNTEVENT, t)

    def updateCounter(self):
        if self.count - 1 > 0:
            self.count -= 1
            self.elements[0].changeText(str(self.count))
        else:
            self.callbacks[2]()


    def handleEvent(self, event):
        if event.type == COUNTEVENT:
            self.updateCounter()
        else:
            for e in self.elements:
                e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())

        return screen