import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
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


def draw():
    screen.fill(BLACK)
    y = 20
    for line in output_lines[-20:]:
        rendered = font.render(line, True, GREEN)
        screen.blit(rendered, (20, y))
        y += 30
    if show_input:
        rendered_input = font.render("> " + input_text + "_", True, GREEN)
        screen.blit(rendered_input, (20, y))
        pygame.display.flip()


def typewriter_effect(text):
    line = ""
    for char in text:
        SM_sound.play()
        time.sleep(0.05)
        line += char
        output_lines.append(line + "_")
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
                typewriter_effect("Antwort wird erstellt. was passiert wenn")
                input_text = ""
                show_input = True

pygame.quit()
sys.exit()
