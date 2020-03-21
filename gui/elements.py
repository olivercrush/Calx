import pygame

class Text:
    def __init__(self, content, pos, size):
        self.pos = pos
        self.element = (pygame.font.Font(None, size)).render(content, True, (0, 0, 0))

    def getElement(self):
        return self.element

    def getRect(self):
        return (self.element).get_rect(center=self.pos)

class Button:
    def __init__(self, content, pos, size, callback):
        self.pos = pos
        self.element = (pygame.font.Font(None, 40)).render(content, True, (200, 200, 200))
        self.callback = callback

    def getElement(self):
        return self.element

    def getRect(self):
        return (self.element).get_rect(center=self.pos)