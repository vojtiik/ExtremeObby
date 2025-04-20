# main.py
# Entry point for the 2D Platformer Game
import pygame
from settings import *
from player import Player
from movement import left, right, stop, up
from level import get_platforms_with_colors, ALL_SOLIDS, START_POS, FINISH_LINE
from ui import draw_text, prompt_name_pygame, draw_win, draw_lose

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Extreme Obby 2D Platformer")
clock = pygame.time.Clock()

# Prompt for player name using Pygame UI
player_name = prompt_name_pygame(screen)

def reset_game():
    global player, game_active, win, lose
    player = Player(*START_POS)
    player.name = player_name
    game_active = True
    win = False
    lose = False

# Create player
player = Player(*START_POS)
player.name = player_name

game_active = True
win = False
lose = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    left(player)
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    right(player)
                if event.key in (pygame.K_UP, pygame.K_w, pygame.K_SPACE):
                    up(player)
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d):
                    stop(player)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()

    if game_active:
        player.update(ALL_SOLIDS)
        # Win condition
        if player.rect.colliderect(FINISH_LINE):
            win = True
            game_active = False
        # Lose condition (fall in pit)
        if player.rect.top > SCREEN_HEIGHT:
            lose = True
            game_active = False

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    # Draw platforms and obstacles with explicit color
    for rect, color, label in get_platforms_with_colors():
        pygame.draw.rect(screen, color, rect)
    # Draw finish line
    pygame.draw.rect(screen, RED, FINISH_LINE)
    # Draw player
    player.draw(screen)
    # Draw player name
    draw_text(screen, player_name, 20, 20)
    # Draw start/finish indicators
    draw_text(screen, "START", 20, SCREEN_HEIGHT - GROUND_HEIGHT - 40)
    draw_text(screen, "FINISH", FINISH_LINE.x - 10, FINISH_LINE.y - 40)
    # Win/Lose messages
    if win:
        draw_win(screen, player_name)
        draw_text(screen, "You made it to the end!", FINISH_LINE.x - 60, FINISH_LINE.y - 60, GREEN)
        draw_text(screen, "Press R to restart", FINISH_LINE.x - 60, FINISH_LINE.y - 20, BLACK)
    if lose:
        draw_lose(screen, player_name)
        draw_text(screen, "Press R to restart", 200, 250)
    pygame.display.flip()
    clock.tick(60)
