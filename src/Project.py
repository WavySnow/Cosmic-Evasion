import os
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
Red = (255, 0, 0)

font = pygame.font.SysFont("arial", 24)


def load_sprite(filename):
    path = os.path.join(os.path.dirname(__file__), "Assets", filename)
    img = pygame.image.load(path).convert_alpha()
    
    
    width, height = img.get_size()
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.get_at((x, y))
            if r > 240 and g > 240 and b > 240:
                img.set_at((x, y), (255, 255, 255, 0))
                
    
    bounding_rect = img.get_bounding_rect()
    return img.subsurface(bounding_rect).copy()

# Load & Scale Sprites
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 60
ship_img = pygame.transform.smoothscale(load_sprite("Halo ship.jpeg"), (PLAYER_WIDTH, PLAYER_HEIGHT))
asteroid_base_img = load_sprite("Asteroid.png")


stars = []
for _ in range(80):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.choice([1, 2, 3])  # Parallax depth: closer stars move faster
    size = 1 if speed == 1 else 2
    brightness = 120 if speed == 1 else (190 if speed == 2 else 255)
    stars.append([x, y, speed, size, brightness])

# Game Variables
player_x = 375
player_y = 500
player_speed = 6

asteroids = []
spawn_counter = 0
score = 0
game_over = False   

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                player_x, player_y = 375, 500
                asteroids = []
                score = 0
                game_over = False

    
    for star in stars:
        star[1] += star[2]  
        if star[1] > HEIGHT:
            star[1] = 0
            star[0] = random.randint(0, WIDTH)

    if not game_over:
        score += 1

        keys = pygame.key.get_pressed()

        # Left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed

        # Right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed

        # Up 
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_y -= player_speed

        # Down 
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_y += player_speed

        # Screen Boundary Collisions 
        if player_x < 0: player_x = 0
        if player_x > WIDTH - PLAYER_WIDTH: player_x = WIDTH - PLAYER_WIDTH
        if player_y < 0: player_y = 0
        if player_y > HEIGHT - PLAYER_HEIGHT: player_y = HEIGHT - PLAYER_HEIGHT

        # Player Hitbox
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT).inflate(-10, -10)

        spawn_counter += 1
        if spawn_counter >= 30:
            ast_size = random.randint(35, 70)
            ast_x = random.randint(0, WIDTH - ast_size)
            ast_rect = pygame.Rect(ast_x, -ast_size, ast_size, ast_size)
            ast_img = pygame.transform.smoothscale(asteroid_base_img, (ast_size, ast_size))
            asteroids.append({"rect": ast_rect, "img": ast_img})
            spawn_counter = 0

        for asteroid in asteroids[:]:
            asteroid["rect"].y += 5

            if asteroid["rect"].top > HEIGHT:
                asteroids.remove(asteroid)
            elif player_rect.colliderect(asteroid["rect"].inflate(-8, -8)):
                game_over = True

    
    screen.fill(Black)

    
    for x, y, speed, size, brightness in stars:
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)

    if not game_over:
       
        screen.blit(ship_img, (player_x, player_y))

        
        for asteroid in asteroids:
            screen.blit(asteroid["img"], asteroid["rect"])

        score_text = font.render(f"Score: {score}", True, White)
        screen.blit(score_text, (20, 20))
    else:
        over_text = font.render("GAME OVER", True, Red)
        restart_text = font.render(f"Final Score: {score} | Press [SPACE] to Restart", True, White)
        screen.blit(over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        screen.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(60)