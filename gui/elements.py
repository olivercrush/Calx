import pygame
import time

class Text:
    def __init__(self, content, pos, size):
        self.pos = pos
        self.element = (pygame.font.Font(None, size)).render(content, True, (0, 0, 0))

    def getElement(self):
        return self.element

    def getRect(self):
        return (self.element).get_rect(center=self.pos)

    def handleEvent(self, event):
        return 0

class Button:
    def __init__(self, content, pos, size, callback):
        self.pos = pos
        self.size = size
        self.callback = callback
        self.text = Text(content, (size[0] / 2, size[1] / 2), 20)
        self.element = self.createElement((155, 155, 155))

    def createElement(self, backgroundColor):
        element = pygame.Surface(self.size)
        element.fill(backgroundColor)
        element.blit(self.text.getElement(), self.text.getRect())
        return element

    def getElement(self):
        return self.element

    def getRect(self):
        return (self.element).get_rect(center=self.pos)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.getRect().collidepoint(event.pos):
                self.element = self.createElement((100, 100, 100))
                if self.callback is not None:
                    self.callback()
        
        if event.type == pygame.MOUSEMOTION:
            if self.getRect().collidepoint(event.pos):
                self.element = self.createElement((140, 140, 140))
            elif not self.getRect().collidepoint(event.pos):
                self.element = self.createElement((155, 155, 155))
        return 0