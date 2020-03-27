import pygame
import gui.mainScreen as mainScreen
import gui.sessionScreen as sessionScreen
import gui.waitingScreen as waitingScreen

class Window:

    def __init__(self):
        pygame.init()

        logo = pygame.image.load("res/icon.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Calx")

        self.size = (800, 600)
        self.callbacks = [
            self.stopApp,
            self.showMainScreen,
            self.showSessionScreen,
            self.showWaitingScreen,
        ]

        self.screen = pygame.display.set_mode(self.size)
        
        self.currentScreen = 0
        self.guiScreens = [
            mainScreen.MainScreen(self.size, self.callbacks),
            sessionScreen.SessionScreen(self.size, self.callbacks),
            waitingScreen.WaitingScreen(self.size, self.callbacks, 6)
        ]


    def startScreen(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.guiScreens[self.currentScreen].handleEvent(event)
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen = self.guiScreens[self.currentScreen].display(self.screen, self.size)
            pygame.display.flip()

    def stopApp(self):
        self.running = False

    def showMainScreen(self):
        self.currentScreen = 0

    def showSessionScreen(self):
        self.currentScreen = 1

    def showWaitingScreen(self):
        self.currentScreen = 2