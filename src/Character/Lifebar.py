from src.utils.terminal import *

class Lifebar():

    def __init__(self, character: "Character"):
        self.character: "Character" = character

        self.health_points: int = character.health_points
        self.max_health_points: int = character.max_health_points 

        self.max_size = 30

    def update(self, character: "Character"):
        self.character: "Character" = character
        self.health_points = self.character.health_points
        self.max_health_points = self.character.max_health_points 

    def __str__(self):
        health_pixels: int = self.max_size * self.character.health_points / self.character.max_health_points
        bar = '['
        for i in range(self.max_size):
            if i <= health_pixels:
                bar += print_square()
            else:
                bar += print_empty_square()
        bar += ']'
        
        if self.character.playable:
            return f"{self.character.name} - lvl.{self.character.level}\n{set_color_green()}{bar}\n                      {self.character.health_points}/{self.character.max_health_points}{set_color_white()}"
        
        return f"{self.character.name} - lvl.{self.character.level}\n{set_color_green()}{bar}\n                      {self.character.health_points}/{self.character.max_health_points}{set_color_white()}"