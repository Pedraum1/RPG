from src.Engine.Phase import Phase
from src.Character.Character import Character

from src.utils.inputs import wait_user
 
class Phase2(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        print("Fase 2 rodando")

        wait_user()
        print("UM INIMIGO APARECEU!")

        wait_user()
        enemy = Character('Wizard')
        
        print(player)
        print(enemy)
        print('')

        while player.is_alive() and enemy.is_alive():
            print(player)
            print(enemy)
            print('')

            wait_user()

            player.attack(enemy)
            enemy.attack(player)

        if player.is_alive():
            print("PLAYER VENCEU O COMBATE!")
        else:
            print("PLAYER PERDEU O COMBATE!")