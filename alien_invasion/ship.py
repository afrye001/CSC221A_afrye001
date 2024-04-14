import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Set the ship's initial position to the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
