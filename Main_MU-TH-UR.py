import pygame
import config


# ============================================================
# 2. HILFSKLASSEN
# ============================================================
class Console:
    """Text-Console für Ausgabe mehrerer Zeilen."""

    def __init__(self, font, color, max_lines):
        self.lines = []
        self.font = font
        self.color = color
        self.max_lines = max_lines

    def add_line(self, text):
        self.lines.append(text)
        if len(self.lines) > self.max_lines:
            self.lines.pop(0)

    def draw(self, surface, x, y):
        for line in self.lines:
            rendered = self.font.render(line, True, self.color)
            surface.blit(rendered, (x, y))
            y += self.font.get_height() + 2


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


# ============================================================
# 3. HAUPTKLASSE
# ============================================================
class MainMuthur:
    def __init__(self):
        # --- Initialisierung ---
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(config.CAP_TXT)

        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.clock = pygame.time.Clock()
        self.black = config.BLACK
        # --- Assets laden ---
        self.font = pygame.font.Font(config.FONT_PATH, config.FONT_SIZE)
        self.SM_sound = pygame.mixer.Sound(config.SM_SOU)
        self.conf_beep = pygame.mixer.Sound(config.CON_SOU)

        # --- Module erstellen ---
        self.console = Console(self.font, config.GREEN, config.MAX_LIN)
        self.cursor = Cursor(
            self.font, config.GREEN, config.CURSOR_BLINK_MS, config.CUR_SYM
        )
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
            if event.type == pygame.QUIT:
                self.running = False
            # Hier später Eingabe-Handling einfügen:
            # elif event.type == pygame.KEYDOWN:
            #     ...

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
        self.console.draw(self.screen, 20, 20)

        # Cursor am Ende der letzten Zeile anzeigen
        cursor_x = 20
        cursor_y = 20 + len(self.console.lines) * (self.font.get_height() + 2)
        self.cursor.draw(self.screen, cursor_x, cursor_y)

        pygame.display.flip()


# ============================================================
# PROGRAMMSTART
# ============================================================
if __name__ == "__main__":
    game = MainMuthur()
    game.main_loop()
