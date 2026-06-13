from src.Character.Role.Role import Role
from src.Character.Character import CharacterStatusDTO

class Warrior(Role):

    def __init__(self):
        super().__init__("Warrior")
    
    def get_base_status(self) -> CharacterStatusDTO:
        status = CharacterStatusDTO()

        status.max_health_points = 690
        status.health_points = 690

        status.attack_damage = 69
        status.physical_defense = 38

        status.magic_damage = 0
        status.magic_defense = 32

        status.critical_rate = 1

        return status
    
    def get_level_progression(self) -> CharacterStatusDTO:
        status = CharacterStatusDTO()

        status.max_health_points = 98
        status.attack_damage = 5
        status.physical_defense = 4
        status.magic_defense = 2

        return status

    # TODO: Criar classes para gerir habilidades especiais das classes