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
spawn_counter = 0
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
                asteroids = []
                score = 0
                game_over = False


    if not game_over:
            score += 1

            keys = pygame.key.get_pressed()

            #  Left
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= player_speed

            # Right
            if keys [pygame.K_RIGHT] or keys [pygame.K_d]:
                player_x += player_speed

            # Up
            if keys [pygame.K_UP] or keys [pygame.K_w]:
               player_x += player_speed

        # Down
            if keys [pygame.K_DOWN] or keys [pygame.K_s]:
               player_x += player_speed

            # Screen Boundary Collisions
            if player_x < 0: player_x = 0
            if player_x > WIDTH - 40: player_x = - 40
            if player_y < 0: player_y = 0
            if player_y > HEIGHT - 40: player_y = HEIGHT - 40

            # Player Hitbox
            player_rect = pygame.Rect(player_x, player_y, 40, 40)

            spawn_counter += 1
            if spawn_counter >= 30:
                ast_size = random.randint(30, 60)
                ast_x = random.randint(0, WIDTH - ast_size)

                asteroids.append(pygame.Rect(ast_x, -ast_size, ast_size, ast_size))
                spawn_counter = 0


            for asteroid in asteroids[:]:
                asteroid.y += 5

                if asteroid.top > HEIGHT:
                    asteroids.remove(asteroid)
                if player_rect.colliderect(asteroid):
                    game_over = True

    screen.fill(Black)

    if game_over:

        pygame.draw.rect(screen, Cyan, player_rect)

        for asteroid in asteroids:
            pygame.draw.rect(screen, Red, asteroid)