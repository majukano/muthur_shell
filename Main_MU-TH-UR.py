import pygame
import config


# ============================================================
# 2. HILFSKLASSEN
# ============================================================
class Console:
    """Text-Console für Ausgabe mehrerer Zeilen."""

    def __init__(self, font, color, max_lines, screen):
        self.lines = []
        self.font = font
        self.color = color
        self.max_lines = max_lines
        self.screen = screen

    def add_line(self, text):
        self.lines.append(text)
        if len(self.lines) > self.max_lines:
            self.lines.pop(0)

    def draw(self, x, y):
        for line in self.lines:
            rendered = self.font.render(line, True, self.color)
            self.screen.blit(rendered, (x, y))
            y += self.font.get_height() + 2
            
    def KI_answer(self, text):
        rendered = self.font.render(text, True, self.color)
        self.screen.blit(rendered,(100,200))
        pygame.display.flip()


class Cursor:
    """Blinkender Cursor."""

    def __init__(self, font, color, blink_time_ms, symbol):
        self.font = font
        self.color = color
        self.symbol = symbol
        self.blink_time_ms = blink_time_ms
        self.timer = 0
        self.visible = False

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.blink_time_ms:
            self.visible = not self.visible
            self.timer = 0

    def draw(self, surface, x, y):
        if self.visible:
            rendered = self.font.render(self.symbol, True, self.color)
            surface.blit(rendered, (x, y))


class KI():
    def __init__(self, Console):
        self.Console = Console
    
    def receive_input(self, input_text):
        self.Console.KI_answer(input_text)


# ============================================================
# 3. HAUPTKLASSE
# ============================================================
class MainMuthur:
    def __init__(self):
        # --- Initialisierung ---
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(config.CAP_TXT)

        self.input_text = ""

        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.black = config.BLACK
        self.green = config.GREEN
        self.cur_sym = config.CUR_SYM
        # --- Assets laden ---
        self.font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)
        self.SM_sound = pygame.mixer.Sound(config.SM_SOU)
        self.conf_beep = pygame.mixer.Sound(config.CON_SOU)

        # --- Module erstellen ---
        self.console = Console(self.font, config.GREEN, config.MAX_LIN, self.screen)
        self.cursor = Cursor(
            self.font, self.green, config.CURSOR_BLINK_MS, self.cur_sym
        )
        self.KI = KI(self.console)

        self.fps = config.FPS
        # --- Erste Ausgabe ---
        self.console.add_line(config.OP_INIT)

        self.running = True

    # -------------------------------
    # Game Loop
    # -------------------------------
    def main_loop(self):
        while self.running:
            dt = self.clock.tick(self.fps)
            self.handle_events()
            self.update(dt)
            self.draw()

    # -------------------------------
    # Events
    # -------------------------------
    def handle_events(self):
        for event in pygame.event.get():
            action = {
                pygame.QUIT: self.quit_game,
                pygame.TEXTINPUT: lambda e=event: self.text_input(e),
                pygame.KEYDOWN: lambda e=event: self.key_down(e),
            }
            action = action.get(event.type)
            if action:
                action()
            # if event.type == pygame.QUIT:
            #     self.running = False
            # Hier später Eingabe-Handling einfügen:
            # elif event.type == pygame.KEYDOWN:
            #     ...

    def quit_game(self):
        self.running = False

    def text_input(self, event):
        self.input_text += event.text

    def key_down(self, event):
        action = {
            pygame.K_BACKSPACE: self.delete_last_charakter,
            pygame.K_RETURN: self.send_input,
        }
        action = action.get(event.key)
        if action:
            action()

    def delete_last_charakter(self):
        self.input_text = self.input_text[:-1]

    def send_input(self):
        self.KI.receive_input(self.input_text)
    # -------------------------------
    # Update
    # -------------------------------
    def update(self, dt):
        self.cursor.update(dt)

    # -------------------------------
    # Render
    # -------------------------------
    def draw(self):
        self.screen.fill(self.black)
        self.console.draw(20, 20)

        # Cursor am Ende der letzten Zeile anzeigen
        cursor_x = 20
        cursor_y = 20 + len(self.console.lines) * (self.font.get_height() + 2)
        if self.input_text == "":
            self.cursor.draw(self.screen, cursor_x, cursor_y)
        else:
            rendered_input = self.font.render(
                self.input_text + self.cur_sym, True, self.green
            )
            self.screen.blit(rendered_input, (20, cursor_y))

        pygame.display.flip()


# ============================================================
# PROGRAMMSTART
# ============================================================
if __name__ == "__main__":
    game = MainMuthur()
    game.main_loop()
