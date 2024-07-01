import pygame
import random
import sys

# Initialisierung
pygame.init()
pygame.font.init()

# Konfigurierbare Spielparameter
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STAR_FREQUENCY = 0.02
MAX_STARS = 5
PLAYER_CHAR = "||"
STAR_CHAR = "*"
SHOOT_CHAR = ":"
PLAYER_LIVES = 3
SHOOT_INTERVAL = 0.3

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Schriftart
font = pygame.font.SysFont("monospace", 35)

# Bildschirm erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sternenschießen")

# Spielerposition
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 50
player_speed = 10

# Spielvariablen
lives = PLAYER_LIVES
score = 0
stars = []
shots = []
last_shot_time = 0
paused = False

clock = pygame.time.Clock()

def draw_text(surface, text, x, y):
    text_surface = font.render(text, True, WHITE)
    surface.blit(text_surface, (x, y))

def pause_game():
    draw_text(screen, "Game Paused", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
    draw_text(screen, "Press any key to resume", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                paused = False

while True:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause_game()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 20:
        player_x += player_speed
    if keys[pygame.K_SPACE] and (pygame.time.get_ticks() - last_shot_time) >= SHOOT_INTERVAL * 1000:
        shots.append([player_x + 10, player_y - 10])
        last_shot_time = pygame.time.get_ticks()

    for shot in shots:
        shot[1] -= 5
    shots = [shot for shot in shots if shot[1] > 0]

    if random.random() < STAR_FREQUENCY and len(stars) < MAX_STARS:
        stars.append([0, random.randint(10, SCREEN_HEIGHT - 50)])

    for star in stars:
        star[0] += 5
    stars = [star for star in stars if star[0] < SCREEN_WIDTH]

    for shot in shots:
        for star in stars:
            if shot[0] in range(star[0], star[0] + 20) and shot[1] in range(star[1], star[1] + 20):
                score += 1
                shots.remove(shot)
                stars.remove(star)
                break

    for star in stars:
        if star[0] >= SCREEN_WIDTH - 20:
            lives -= 1
            stars.remove(star)
            if lives == 0:
                screen.fill(BLACK)
                draw_text(screen, "Game Over!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
                draw_text(screen, "Press Q to Quit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
                pygame.display.flip()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

    draw_text(screen, PLAYER_CHAR, player_x, player_y)
    for star in stars:
        draw_text(screen, STAR_CHAR, star[0], star[1])
    for shot in shots:
        draw_text(screen, SHOOT_CHAR, shot[0], shot[1])

    draw_text(screen, f"Score: {score}", 10, 10)
    draw_text(screen, f"Lives: {lives}", 10, 50)

    pygame.display.flip()
    clock.tick(30)
