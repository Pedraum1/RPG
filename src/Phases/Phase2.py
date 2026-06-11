from src.Engine.Phase import Phase
from src.Character.Character import Character

from src.Engine.Combat import Combat

from src.utils.inputs import wait_user
 
class Phase2(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        print("Fase 2 rodando")

        Combat().run(player, [Character('Warrior')])
