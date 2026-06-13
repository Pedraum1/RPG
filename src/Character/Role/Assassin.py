from src.Character.Role.Role import Role
from src.Character.Character import CharacterStatusDTO

class Assassin(Role):

    def __init__(self):
        super().__init__("Assassin")

    def get_base_status(self):
        status = CharacterStatusDTO()

        status.max_health_points = 654
        status.health_points = 654

        status.attack_damage = 63
        status.physical_defense = 32

        status.magic_damage = 0
        status.magic_defense = 29

        status.critical_rate = 25

        return status