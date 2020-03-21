import pygame

class Window:

    def __init__(self):
        pygame.init()

        logo = pygame.image.load("res/icon.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Calx")

        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)

        font = pygame.font.Font(None, 48)
        self.title = font.render("CALX", True, (0, 0, 0))
        font = pygame.font.Font(None, 26)
        self.undertitle = font.render("The Personal Math Trainer", True, (0, 0, 0))

    def startScreen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((245, 245, 245))
            self.screen.blit(self.title, (self.size[0] / 2 - self.title.get_width() / 2, 30))
            self.screen.blit(self.undertitle, (self.size[0] / 2 - self.undertitle.get_width() / 2, 80))
            pygame.display.flip()