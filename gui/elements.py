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
        self.size = size
        self.callback = callback
        self.text = Text(content, (size[0] / 2, size[1] / 2), 20)
        self.element = self.createElement()

    def createElement(self):
        element = pygame.Surface(self.size)
        element.fill((155, 155, 155))
        element.blit(self.text.getElement(), self.text.getRect())
        return element

    def getElement(self):
        return self.element

    def getRect(self):
        return (self.element).get_rect(center=self.pos)