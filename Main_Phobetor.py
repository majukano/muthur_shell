import pygame
import sys
import config
import time


class Console:
    def __init__(self, TextInput, TextGen, KIOutput):
        self.KIOutput = KIOutput
        self.TextInput = TextInput
        self.TextGen = TextGen
        self.WIDTH = config.WIDTH
        self.HEIGHT = config.HEIGHT
        self.BLACK = config.BLACK
        self.GREEN = config.GREEN
        self.CAP_TXT = config.CAP_TXT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.CAP_TXT)
        self.screen.fill((self.BLACK))
        self.area_calc()
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
        self.kioutput_area_pos = (50, 250)

    def top_area(self):
        init_text = self.TextInput.top_text_input()
        top_text = self.TextGen.top_text(init_text)
        self.screen.blit(top_text, self.top_font_pos)

    def cursor_area(self, dt):
        cursor_text = self.TextInput.cursor_text_input(dt)
        cursor_ren_text = self.TextGen.top_text(cursor_text)
        self.screen.blit(cursor_ren_text, self.cursor_area_pos)

    def output_area(self, dt):
        output_data = self.KIOutput.rendert_output(dt)
        self.screen.blit(output_data, self.kioutput_area_pos)

    def screen_reset(self):
        self.screen.fill((0, 0, 0))  # Schwarz, oder jede beliebige Farbe


class Loop:
    def __init__(self, Console, TextInput, KIOutput, clock, fps):
        self.TextInput = TextInput
        self.KIOutput = KIOutput
        self.clock = clock
        self.fps = fps
        self.Console = Console
        self.dt = 0
        self.main_loop()

    def main_loop(self):
        while True:
            self.dt = self.clock.tick(self.fps)
            self.Console.screen_reset()
            self.handle_events()
            self.Console.main_lines()
            self.Console.top_area()
            self.Console.cursor_area(self.dt)
            self.Console.output_area(self.dt)
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            action = {
                pygame.QUIT: self.quit_game,
                pygame.TEXTINPUT: lambda e=event: self.TextInput.new_txt(e),
                pygame.KEYDOWN: lambda e=event: self.key_down(e),
            }
            action = action.get(event.type)
            if action:
                action()

    def key_down(self, event):
        action = {
            pygame.K_BACKSPACE: self.TextInput.delete_last_charakter,
            pygame.K_RETURN: self.KIOutput.get_input,
        }
        action = action.get(event.key)
        if action:
            action()

    def quit_game(self):
        pygame.quit()
        sys.exit()


class TextInput:
    def __init__(self):
        self.OP_INIT = config.OP_INIT
        self.CUR_SYM = config.CUR_SYM
        self.cursor_timer = 0
        self.cursor_visible = False
        self.blink_time_ms = config.CURSOR_BLINK_MS
        self.input_text = ""

    def top_text_input(self):
        return self.OP_INIT

    def cursor_text_input(self, dt):
        if self.input_text == "":
            self.cursor_blink(dt)
            cursor_text = ""
            if self.cursor_visible:
                cursor_text = self.CUR_SYM
        else:
            cursor_text = self.input_text + self.CUR_SYM
        return cursor_text

    def cursor_blink(self, dt):
        self.cursor_timer += dt
        if self.cursor_timer >= self.blink_time_ms:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def new_txt(self, textinput_event):
        self.input_text += textinput_event.text

    def delete_last_charakter(self):
        self.input_text = self.input_text[:-1]

    def send_input_txt(self):
        return self.input_text


class KIOutput:
    def __init__(self, TextInput, TextGen):
        self.TextInput = TextInput
        self.TextGen = TextGen
        self.input_txt = ""
        self.output = ""
        self.typrewriter_num = 0
        self.typrewriter_slow_fact = config.TW_SL
        self.typrewriter_slower = 0
        self.new_request = False

    def get_input(self):
        self.input_txt = self.TextInput.send_input_txt()
        self.output = ""
        self.new_request = True
        self.typrewriter_num = 0
        self.typrewriter_slower = 0

    def rendert_output(self, dt):
        if self.new_request:
            self.typewriter_effekt(self.input_txt, dt)
        self.ren_output = self.TextGen.top_text(self.output)
        return self.ren_output

    def typewriter_effekt(self, text, dt):
        text_len = len(text)
        if self.typrewriter_num < text_len:
            if self.typrewriter_slower % self.typrewriter_slow_fact == 0:
                self.output += text[self.typrewriter_num]
                self.typrewriter_num += 1
        else:
            self.new_request = False
        self.typrewriter_slower += 1


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
        self.TextGen = TextGen()
        self.TextInput = TextInput()
        self.KIOutput = KIOutput(self.TextInput, self.TextGen)
        self.Console = Console(self.TextInput, self.TextGen, self.KIOutput)
        Loop(self.Console, self.TextInput, self.KIOutput, self.clock, self.fps)


if __name__ == "__main__":
    MainPhobetor()
