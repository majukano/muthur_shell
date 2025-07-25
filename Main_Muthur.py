import pygame
import sys
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MU-TH-UR Android")

# Android: Tastatur zeigen
pygame.key.start_text_input()

font = pygame.font.SysFont("couriernew", 24)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

input_text = ""
output_lines = ["MU-TH-UR 6000 READY FOR INPUT"]

show_input = True

pygame.init()
pygame.mixer.init()
SM_sound = pygame.mixer.Sound("SM_sound.mp3")
conf_beep = pygame.mixer.Sound("conf_beep.ogg")

courser = "\u2588"

line_y = HEIGHT // 2  # y-Position (horizontal in der Mitte)
start_x = WIDTH  # Start am rechten Rand
end_x = 100  # Verschwinde bei x < 200
speed = 10  # Geschwindigkeit der Bewegung


def draw():
    screen.fill(BLACK)
    y = 20
    for line in output_lines[-20:]:
        rendered = font.render(line, True, GREEN)
        screen.blit(rendered, (20, y))
        y += 30
    if show_input:
        rendered_input = font.render("> " + input_text + courser, True, GREEN)
        screen.blit(rendered_input, (20, y))
        pygame.display.flip()


def output_line(start_x, line_y):
    while start_x > end_x:
        pygame.draw.line(
            screen, (0, 255, 0), (start_x, line_y), (start_x - 100, line_y), 10
        )
        start_x -= speed
        pygame.display.flip()
    conf_beep.play()
    time.sleep(0.1)


def typewriter_effect(text):
    line = ""
    for char in text:
        SM_sound.play()
        time.sleep(0.05)
        line += char
        output_lines.append(line + courser)
        draw()
        pygame.display.flip()
        output_lines.pop()
    output_lines.append(line)


# Main Loop
running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.TEXTINPUT:
            input_text += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                output_lines.append("> " + input_text)
                show_input = False
                line_y = 30 + len(output_lines) * (font.get_height() + 2)
                output_line(start_x, line_y)
                typewriter_effect("Antwort wird erstellt. was passiert wenn")
                input_text = ""
                show_input = True

pygame.quit()
sys.exit()
