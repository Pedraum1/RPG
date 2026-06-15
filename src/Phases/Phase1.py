from src.Engine.Phase import Phase
from src.Character.Character import Character
from src.utils.inputs import wait_user

from src.utils.time import delay
from src.utils.terminal import clear_terminal
 
class Phase1(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        clear_terminal()

        print("Fase 1 rodando")
        print(player)
        print('')

        delay()

        player.level_up(2)
        print(f"{player.name} subiu 2 níveis")
        wait_user()
        