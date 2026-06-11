from random import randint

class CharacterStatusDTO():
        
    def __init__(self):
        self.health_points: int
        self.max_health_points: int

        self.attack_damage: int
        self.magic_damage: int
        self.physical_defense: int
        self.magic_defense: int
        self.critical_rate: int

class Character():

    def __init__(self, role: str):

        self.health_points: int
        self.max_health_points: int

        self.attack_damage: int
        self.magic_damage: int
        self.physical_defense: int
        self.magic_defense: int
        self.critical_rate: int

        Status: CharacterStatusDTO = self.generateStatus(role)
        self.apply_status(Status)

        self.role: str = role

    def apply_status(self, Status: CharacterStatusDTO) -> None:
        self.health_points     = Status.health_points
        self.max_health_points = Status.max_health_points
        self.attack_damage     = Status.attack_damage
        self.magic_damage      = Status.magic_damage
        self.physical_defense  = Status.physical_defense
        self.magic_defense     = Status.magic_defense
        self.critical_rate     = Status.critical_rate

    def attack(self, target: "Character"):
        damage: int = self.calculate_damage(self.attack_damage, target.physical_defense)
        if self.attackWillCrit():
            damage *= 2
        target.receive_damage(damage)

    def receive_damage(self, damage: int):
        self.health_points = max(0, self.health_points - damage)
    
    def calculate_damage(self, damage: int, defense: int) -> int:
        return round(damage * 100 / (100+defense))

    def attackWillCrit(self):
        return self.critical_rate > randint(0, 99)
    
    def is_alive(self):
        return self.health_points > 0
    
    def is_dead(self):
        return not self.is_alive()
    
    def generateStatus(self, role: str) -> CharacterStatusDTO:
        status = CharacterStatusDTO()
        match role:
            case "Warrior":
                status.max_health_points = 1000
                status.health_points = 1000

                status.attack_damage = 100
                status.physical_defense = 70

                status.magic_damage = 0
                status.magic_defense = 40

                status.critical_rate = 1

            case "Wizard":
                status.max_health_points = 550
                status.health_points = 550

                status.attack_damage = 40
                status.physical_defense = 40

                status.magic_damage = 140
                status.magic_defense = 30

                status.critical_rate = 0
        
        return status
    
    def __str__(self):
        return f"{self.role} | {self.health_points}/{self.max_health_points}"