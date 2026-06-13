from src.Character.Role.Role import Role
from src.Character.Character import CharacterStatusDTO

class Mage(Role):

    def __init__(self):
        super().__init__("Mage")
    
    def get_base_status(self):
        status = CharacterStatusDTO()

        status.max_health_points = 630
        status.health_points = 630

        status.attack_damage = 56
        status.physical_defense = 25

        status.magic_damage = 20
        status.magic_defense = 30

        status.critical_rate = 0

        return status
    
    def get_level_progression(self) -> CharacterStatusDTO:
        status = CharacterStatusDTO()

        status.max_health_points = 98
        status.attack_damage = 5
        status.physical_defense = 4
        status.magic_defense = 2

        return status