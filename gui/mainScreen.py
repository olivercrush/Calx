import pygame

class MainScreen:

    def __init__(self):
        font = pygame.font.Font(None, 48)
        self.title = font.render("CALX", True, (0, 0, 0))
        font = pygame.font.Font(None, 26)
        self.undertitle = font.render("The Personal Math Trainer", True, (0, 0, 0))
        font = pygame.font.Font(None, 16)
        self.info = font.render("by @olivercrush (github)", True, (0, 0, 0))

    def display(self, screen, size):
        screen.fill((245, 245, 245))
        screen.blit(self.title, (size[0] / 2 - self.title.get_width() / 2, 30))
        screen.blit(self.undertitle, (size[0] / 2 - self.undertitle.get_width() / 2, 80))
        screen.blit(self.info, (size[0] - self.info.get_width() - 5, size[1] - self.info.get_height() - 5))
        return screen