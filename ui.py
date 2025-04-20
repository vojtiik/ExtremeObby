# ui.py
# User interface functions
import pygame
from settings import FONT_NAME, FONT_SIZE, BLACK, RED, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def draw_text(surface, text, x, y, color=BLACK):
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    text_surf = font.render(text, True, color)
    surface.blit(text_surf, (x, y))

def prompt_name_pygame(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
    input_box = pygame.Rect(SCREEN_WIDTH//2-150, SCREEN_HEIGHT//2-32, 300, 48)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    name = ''
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if name.strip() != '':
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 16 and event.unicode.isprintable():
                            name += event.unicode
        screen.fill(WHITE)
        draw_text(screen, "Enter your username:", SCREEN_WIDTH//2-140, SCREEN_HEIGHT//2-90)
        txt_surface = font.render(name, True, color)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+8))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
    return name or "Player"

def draw_win(surface, name):
    draw_text(surface, f"Congratulations {name}, you win!", 200, 200, RED)

def draw_lose(surface, name):
    draw_text(surface, f"Sorry {name}, you fell!", 200, 200, RED)
