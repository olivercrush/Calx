import pygame
import gui.elements as elements
import time

COUNTEVENT = pygame.USEREVENT+1
t = 1000

class EndSessionScreen:

    def __init__(self, size, callbacks, result = 0):
        self.count = 3
        self.callbacks = callbacks

        self.background = (245, 245, 245)
        self.elements = [
            elements.Text("Fin de la session", (size[0] / 2, 170), 50, 1),
            elements.Text("Moyenne de temps de réponse : " + str(result) + "s", (size[0] / 2, 220), 40, 1),
        ]

        pygame.time.set_timer(COUNTEVENT, t)

    def updateCounter(self):
        if self.count - 1 > 0:
            self.count -= 1
        else:
            self.callbacks[1]()


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