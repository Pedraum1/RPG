from src.Character.Character import Character
from src.Character.Role.Warrior import Warrior

from src.Engine.Phase import Phase

from src.Phases.Phase1 import Phase1
from src.Phases.Phase2 import Phase2
from src.Phases.Phase3 import Phase3

from src.utils.time import delay


class Engine():

    def __init__(self):
        self.phases: list[Phase] = []

        self.phases.append(Phase1())
        self.phases.append(Phase2())
        self.phases.append(Phase3())

        character_name = input("Escolha o nome do seu personagem:\n")
        player_class = Warrior()
        player: Character = Character(player_class, character_name)

        delay()

        self.run(player)
        
    def run(self, player: Character):
        for phase in self.phases:
            phase.run(player)
            
            if player.is_dead():
                print("GAME OVER")
                break