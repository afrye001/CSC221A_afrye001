import sys
import pygame

from settings import Settings


class AlienInvasion:

    """Overall class to manage game assets and behavior."""

    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
  
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = pygame.image.load("assets/ship-final-2.bmp")
        self.ship = pygame.image.load("assets/ship-final-2.bmp").convert_alpha()


    def run_game(self):
        # Watch for Keyboard and Mouse events
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # Make the most recently drawn screen visible 
        pygame.display.flip()
        self.clock.tick(60) 
        # Redraw the screen, fill with background color 
        self.screen.fill(self.bg_color) 

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()