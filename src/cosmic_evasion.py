import pygame
import sys
import random

pygame.init()

# Window Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Evasion - Dual Controls")
clock = pygame.time.Clock()

# Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Cyan = (0, 255, 255)
Red = (255, 0, 0)


font = pygame.font.sysfont("arial", 24)

# Game Variables
player_x = 380
player_y = 500
player_speed = 6


astroids = []
spwan_counter = 0
score = 0
game_over = False   


# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()


        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                player_x, player_y = 380, 500
                astroids = []
                score = 0
                game_over = False