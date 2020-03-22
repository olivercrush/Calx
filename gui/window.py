import pygame
import gui.mainScreen as mainScreen

class Window:

    def __init__(self):
        pygame.init()

        logo = pygame.image.load("res/icon.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Calx")

        self.size = (800, 600)
        self.callbacks = [
            self.stopApp
        ]

        self.screen = pygame.display.set_mode(self.size)
        
        self.mScreen = mainScreen.MainScreen(self.size, self.callbacks)

    def startScreen(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.mScreen.handleEvent(event)
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen = self.mScreen.display(self.screen, self.size)

            pygame.display.flip()

    def stopApp(self):
        self.running = False