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
                bar += '#'
            else:
                bar += ' '
        bar += ']'
        
        return f"{self.character.name} - lvl.{self.character.level}\n{bar}\n                      {self.character.health_points}/{self.character.max_health_points}"