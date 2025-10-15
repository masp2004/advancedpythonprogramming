"""
Star Shooting Game - A simple pygame-based shooting game.

This module implements a game where the player shoots at stars moving across
the screen. The player controls a ship that can move left/right and shoot
projectiles to hit incoming stars.

Features:
- Configurable game parameters
- Score tracking
- Lives system
- Pause functionality
- Game over screen

Controls:
- LEFT/RIGHT arrows: Move player
- SPACE: Shoot
- P: Pause game
- Q: Quit (on game over screen)
"""

import pygame
import random
import sys
from typing import List, Tuple

# Pygame initialization
pygame.init()
pygame.font.init()

# Configurable game parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STAR_FREQUENCY = 0.02
MAX_STARS = 5
PLAYER_CHAR = "||"
STAR_CHAR = "*"
SHOOT_CHAR = ":"
PLAYER_LIVES = 3
SHOOT_INTERVAL = 0.3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("monospace", 35)


class GameObject:
    """Base class for game objects with position."""
    
    def __init__(self, x: int, y: int):
        """
        Initialize a game object.
        
        Args:
            x (int): Initial x coordinate.
            y (int): Initial y coordinate.
        """
        self.x = x
        self.y = y
    
    def get_position(self) -> List[int]:
        """Get current position as [x, y] list."""
        return [self.x, self.y]
    
    def set_position(self, x: int, y: int) -> None:
        """Set position to new coordinates."""
        self.x = x
        self.y = y


class Player(GameObject):
    """Represents the player's ship."""
    
    def __init__(self, x: int, y: int, speed: int = 10):
        """
        Initialize the player.
        
        Args:
            x (int): Initial x coordinate.
            y (int): Initial y coordinate.
            speed (int): Movement speed in pixels per frame.
        """
        super().__init__(x, y)
        self.speed = speed
    
    def move_left(self) -> None:
        """Move player left by speed amount, respecting screen bounds."""
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self, max_x: int) -> None:
        """
        Move player right by speed amount, respecting screen bounds.
        
        Args:
            max_x (int): Maximum x coordinate (screen width - player width).
        """
        if self.x < max_x - 20:
            self.x += self.speed


class GameManager:
    """Main game manager handling game state and logic."""
    
    def __init__(self):
        """Initialize the game manager with default state."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sternenschießen")
        
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.lives = PLAYER_LIVES
        self.score = 0
        self.stars: List[List[int]] = []
        self.shots: List[List[int]] = []
        self.last_shot_time = 0
        self.clock = pygame.time.Clock()
    
    def draw_text(self, text: str, x: int, y: int) -> None:
        """
        Draw text on the screen.
        
        Args:
            text (str): The text to display.
            x (int): X coordinate.
            y (int): Y coordinate.
        """
        text_surface = font.render(text, True, WHITE)
        self.screen.blit(text_surface, (x, y))
    
    def pause_game(self) -> None:
        """Display pause screen and wait for user input."""
        self.draw_text("Game Paused", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        self.draw_text("Press any key to resume", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    paused = False
    
    def handle_input(self) -> None:
        """Process keyboard input for player movement and actions."""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right(SCREEN_WIDTH)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self) -> None:
        """Create a new shot if enough time has passed since last shot."""
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_shot_time) >= SHOOT_INTERVAL * 1000:
            self.shots.append([self.player.x + 10, self.player.y - 10])
            self.last_shot_time = current_time
    
    def update_shots(self) -> None:
        """Move shots upward and remove off-screen shots."""
        for shot in self.shots:
            shot[1] -= 5
        self.shots = [shot for shot in self.shots if shot[1] > 0]
    
    def spawn_stars(self) -> None:
        """Randomly spawn new stars at the left edge of the screen."""
        if random.random() < STAR_FREQUENCY and len(self.stars) < MAX_STARS:
            self.stars.append([0, random.randint(10, SCREEN_HEIGHT - 50)])
    
    def update_stars(self) -> None:
        """Move stars to the right and remove off-screen stars."""
        for star in self.stars:
            star[0] += 5
        
        # Remove stars that reached the right edge and decrease lives
        stars_to_remove = []
        for star in self.stars:
            if star[0] >= SCREEN_WIDTH - 20:
                stars_to_remove.append(star)
                self.lives -= 1
        
        for star in stars_to_remove:
            self.stars.remove(star)
    
    def check_collisions(self) -> None:
        """Check for collisions between shots and stars."""
        shots_to_remove = []
        stars_to_remove = []
        
        for shot in self.shots:
            for star in self.stars:
                if (shot[0] in range(star[0], star[0] + 20) and 
                    shot[1] in range(star[1], star[1] + 20)):
                    self.score += 1
                    if shot not in shots_to_remove:
                        shots_to_remove.append(shot)
                    if star not in stars_to_remove:
                        stars_to_remove.append(star)
                    break
        
        for shot in shots_to_remove:
            if shot in self.shots:
                self.shots.remove(shot)
        for star in stars_to_remove:
            if star in self.stars:
                self.stars.remove(star)
    
    def draw_game_objects(self) -> None:
        """Draw all game objects on the screen."""
        self.draw_text(PLAYER_CHAR, self.player.x, self.player.y)
        
        for star in self.stars:
            self.draw_text(STAR_CHAR, star[0], star[1])
        
        for shot in self.shots:
            self.draw_text(SHOOT_CHAR, shot[0], shot[1])
    
    def draw_ui(self) -> None:
        """Draw the user interface (score and lives)."""
        self.draw_text(f"Score: {self.score}", 10, 10)
        self.draw_text(f"Lives: {self.lives}", 10, 50)
    
    def game_over(self) -> None:
        """Display game over screen and wait for quit."""
        self.screen.fill(BLACK)
        self.draw_text("Game Over!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        self.draw_text("Press Q to Quit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    
    def run(self) -> None:
        """Main game loop."""
        while True:
            self.screen.fill(BLACK)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause_game()
            
            # Input handling
            self.handle_input()
            
            # Update game state
            self.update_shots()
            self.spawn_stars()
            self.update_stars()
            self.check_collisions()
            
            # Check game over condition
            if self.lives <= 0:
                self.game_over()
            
            # Draw everything
            self.draw_game_objects()
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(30)


def main() -> None:
    """Main entry point for the game."""
    game = GameManager()
    game.run()


if __name__ == "__main__":
    main()

