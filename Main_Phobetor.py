import pygame
import sys
import config


class Console:
    def __init__(self):
        self.TextInput = TextInput()
        self.TextGen = TextGen()
        self.WIDTH = config.WIDTH
        self.HEIGHT = config.HEIGHT
        self.BLACK = config.BLACK
        self.GREEN = config.GREEN
        self.CAP_TXT = config.CAP_TXT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.CAP_TXT)
        self.screen.fill((self.BLACK))
        self.area_calc()
        self.main_lines()
        self.area_prep()

    def area_calc(self):
        self.top_area_height = 100
        self.right_area = self.WIDTH - 200
        self.foot_area = self.HEIGHT - 100

    def main_lines(self):
        # TOP AREA LINE
        pygame.draw.line(
            self.screen,
            self.GREEN,
            (0, self.top_area_height),
            (self.WIDTH, self.top_area_height),
            2,
        )

        # RIGHT AREA LINE
        pygame.draw.line(
            self.screen,
            self.GREEN,
            (self.right_area, 0),
            (self.right_area, self.HEIGHT),
            2,
        )

        pygame.draw.line(
            self.screen,
            self.GREEN,
            (0, self.foot_area),
            (self.WIDTH, self.foot_area),
            2,
        )

    def area_prep(self):
        self.top_font_pos = (50, 50)
        self.cursor_area_pos = (50, 125)

    def top_area(self):
        init_text = self.TextInput.top_text_input()
        top_text = self.TextGen.top_text(init_text)
        self.screen.blit(top_text, self.top_font_pos)

    def cursor_area(self):
        cursor_text = self.TextInput.cursor_text_input()
        cursor_ren_text = self.TextGen.top_text(cursor_text)
        self.screen.blit(cursor_ren_text, self.cursor_area_pos)


class Loop:
    def __init__(self, Console, clock, fps):
        self.clock = clock
        self.fps = fps
        self.Console = Console
        self.main_loop()

    def main_loop(self):
        while True:
            dt = self.clock.tick(self.fps)
            self.handle_events()
            self.Console.top_area()
            self.Console.cursor_area()
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


class TextInput:
    def __init__(self):
        self.OP_INIT = config.OP_INIT
        self.CUR_SYM = config.CUR_SYM

    def top_text_input(self):
        return self.OP_INIT

    def cursor_text_input(self):
        return self.CUR_SYM


class TextGen:
    def __init__(self):
        self.GREEN = config.GREEN
        self.FONT_PATH = config.FONT_PATH
        self.FONT_SIZE = config.FONT_SIZE
        self.top_font = pygame.font.Font(self.FONT_PATH, self.FONT_SIZE)

    def top_text(self, input_text):
        t_text = self.top_font.render(input_text, True, self.GREEN)
        return t_text


class MainPhobetor:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = config.FPS
        self.Console = Console()
        Loop(self.Console, self.clock, self.fps)


if __name__ == "__main__":
    MainPhobetor()
