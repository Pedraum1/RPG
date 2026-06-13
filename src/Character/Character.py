from random import randint
from src.Character.Lifebar import Lifebar
from src.utils.inputs import wait_user

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

    def __init__(self, role: str, name:str = ""):

        self.health_points: int
        self.max_health_points: int

        self.attack_damage: int
        self.magic_damage: int
        self.physical_defense: int
        self.magic_defense: int
        self.critical_rate: int

        self.name:str = name
        self.role: str = role

        Status: CharacterStatusDTO = self.generateStatus(role)
        self.apply_status(Status)

        self.level: int = 1
        self.lifebar: Lifebar = Lifebar(self)

        self.playable: bool = False


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
        print(f"{self.name} IRÁ ATACAR {target.name}")
        wait_user()

        if self.attackWillCrit():
            damage *= 2
            print("ATAQUE CRÍTICO!")
            wait_user()
        target.receive_damage(damage)
        wait_user()

    def receive_damage(self, damage: int):
        print(f"{self.name} recebeu {damage} de dano")
        self.health_points = max(0, self.health_points - damage)
        self.lifebar.update(self)
    
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
    
    def set_playable(self):
        self.playable = True
    
    def __str__(self):
        return f"{self.name} - {self.level} | {self.health_points}/{self.max_health_points}"