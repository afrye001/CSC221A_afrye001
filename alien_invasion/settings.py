import sys
import pygame

class Settings: 
    """A class to store all settings for Alien Invasion""" 

    def __init__(self): 
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800 
        
        self.bg_color = (230, 230, 230)

        # TIY 12-1: BLUE SKY
        #self.bg_color = (000, 000, 120)

        # alternative background color 
        #self.bg_color = (0, 20, 255) 
        
        