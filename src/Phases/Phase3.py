from src.Engine.Phase import Phase
from src.Character.Character import Character
from src.utils.inputs import wait_user

class Phase3(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        print("Fase 3 rodando")
        print(player)
        print('')

        wait_user()