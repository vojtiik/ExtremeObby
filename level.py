# level.py
# Level layout and platforms
import pygame
from settings import SCREEN_HEIGHT, GROUND_HEIGHT, OBSTACLE_COLOR, PLATFORM_COLOR, BLUE, GREEN, RED, GRAY

# Each platform/obstacle is now a tuple: (pygame.Rect, color, label)
PLATFORM_LIST = [
    # Start platform
    (pygame.Rect(0, SCREEN_HEIGHT - GROUND_HEIGHT, 300, GROUND_HEIGHT), GREEN, "Start platform"),
    # Matthew's block 1
    (pygame.Rect(250, SCREEN_HEIGHT - GROUND_HEIGHT - 40, 40, 40), BLUE, "Matthew's block 1"),
    # Single block
    (pygame.Rect(350, SCREEN_HEIGHT - GROUND_HEIGHT - 40, 40, 40), GRAY, "Single block"),
    # High jump
    (pygame.Rect(423, SCREEN_HEIGHT - GROUND_HEIGHT - 124, 40, 180), RED, "High jump"),
    # Double blocks
    (pygame.Rect(500, SCREEN_HEIGHT - GROUND_HEIGHT - 80, 40, 80), GRAY, "Double blocks"),
    # Mid platform
    (pygame.Rect(600, SCREEN_HEIGHT - GROUND_HEIGHT, 120, GROUND_HEIGHT), GREEN, "Mid platform"),
    # End platform
    (pygame.Rect(800, SCREEN_HEIGHT - GROUND_HEIGHT, 300, GROUND_HEIGHT), GREEN, "End platform"),
]

START_POS = (20, SCREEN_HEIGHT - GROUND_HEIGHT - 40)
# Move the finish line to the visible end of the end platform
FINISH_LINE = pygame.Rect(750, SCREEN_HEIGHT - GROUND_HEIGHT - 60, 20, 100)

# For collision detection
PLATFORMS = [PLATFORM_LIST[0][0], PLATFORM_LIST[5][0], PLATFORM_LIST[6][0]]
OBSTACLES = [PLATFORM_LIST[1][0], PLATFORM_LIST[2][0], PLATFORM_LIST[3][0], PLATFORM_LIST[4][0]]

ALL_SOLIDS = [plat[0] for plat in PLATFORM_LIST]

def get_platforms_with_colors():
    return PLATFORM_LIST
