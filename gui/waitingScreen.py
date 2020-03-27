import pygame
import gui.elements as elements
import time

class WaitingScreen:

    def __init__(self, size, callbacks, count):
        self.count = count
        self.callbacks = callbacks

        self.background = (245, 245, 245)
        self.elements = [
            elements.Text(str(count), (size[0] / 2, 170), 50, 1),
        ]

    def updateCounter(self):
        if self.count - 1 > 0:
            self.count -= 1
            self.elements[0].changeText(str(self.count))
        else:
            self.callbacks[2]()

    def handleEvent(self, event):
        for e in self.elements:
            e.handleEvent(event)

    def display(self, screen, size):
        screen.fill(self.background)

        self.updateCounter()
        time.sleep(1)

        for e in self.elements:
            screen.blit(e.getElement(), e.getRect())


        return screen