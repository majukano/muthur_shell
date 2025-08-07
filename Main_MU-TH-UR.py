import pygame
import sys
import time


class MainMuthur:
    def __init__(self):
        pygame.init()
        self.SM_sound = pygame.mixer.Sound("SM_sound.mp3")
        self.conf_beep = pygame.mixer.Sound("conf_beep.ogg")
        font_path = "fonts/TerminessNerdFontMono-Regular.ttf"
        self.font = pygame.font.Font(font_path, 16)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.COURSER = "\u2588"
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("MU-TH-UR Android")
        self.output_init = ["MU-TH-UR 6000 READY FOR INPUT"]
        self.main_loop()

    def main_loop(self):
        running = True
        while running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # elif event.type == pygame.TEXTINPUT:
                #     input_text += event.text
                # elif event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_BACKSPACE:
                #         input_text = input_text[:-1]
                #     elif event.key == pygame.K_RETURN:
                #         output_lines.append("> " + input_text)
                #         show_input = False
                #         line_y = 30 + len(output_lines) * (font.get_height() + 2)
                #         output_line(start_x, line_y)
                #         typewriter_effect("Antwort wird erstellt. was passiert wenn")
                #         input_text = ""
                #         show_input = True

    def draw(self):
        self.screen.fill(self.BLACK)
        y = 20
        for line in self.output_init[-20:]:
            rendered = self.font.render(line, True, self.GREEN)
            self.screen.blit(rendered, (20, y))
            y += 30
        # rendered_input = self.font.render("> " + input_text + courser, True, GREEN)
        # self.screen.blit(rendered_input, (20, y))
        pygame.display.flip()


if __name__ == "__main__":
    MainMuthur()
