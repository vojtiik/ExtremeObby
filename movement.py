# movement.py
# Functions for player movement
import pygame
from settings import PLAYER_SPEED, PLAYER_JUMP_VELOCITY

def left(player):
    player.vel_x = -PLAYER_SPEED

def right(player):
    player.vel_x = PLAYER_SPEED

def stop(player):
    player.vel_x = 0

def up(player):
    # Jump only if on ground
    if player.on_ground:
        player.vel_y = PLAYER_JUMP_VELOCITY
        player.on_ground = False
