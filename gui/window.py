import pygame
import gui.mainScreen as mainScreen

class Window:

    def __init__(self):
        pygame.init()

        logo = pygame.image.load("res/icon.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Calx")

        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)

        self.mScreen = mainScreen.MainScreen()

    def startScreen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen = self.mScreen.display(self.screen, self.size)

            pygame.display.flip()