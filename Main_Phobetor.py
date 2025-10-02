import pygame
import sys
import config


class Console:
    def __init__(self, screen):
        self.BLACK = config.BLACK
        screen.fill((self.BLACK))


class Loop:
    def __init__(self):
        self.main_loop()

    def main_loop(self):
        while True:
            self.handle_events()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            action = {pygame.QUIT: self.quit_game}
            action = action.get(event.type)
            if action:
                action()

    def quit_game(self):
        pygame.quit()
        sys.exit()


class MainPhobetor:
    def __init__(self):
        pygame.init()
        self.WIDTH = config.WIDTH
        self.HEIGHT = config.HEIGHT
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Phobetor Station")
        Console(screen)
        Loop()


if __name__ == "__main__":
    MainPhobetor()
