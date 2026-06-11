from src.Character.Character import Character
from src.utils.inputs import wait_user

class Combat():

    def run(self, player: Character, enemies: list[Character]) -> None:
        
        if(len(enemies) > 1):
            print(f"{len(enemies)} INIMIGOS APARECERAM!")
        else:
            print("UM INIMIGO APARECEU!")

        wait_user()

        while player.is_alive() and self.any_enemies_alive(enemies):

            for enemy in enemies:

                self.print_combatants(player, enemy)

                turn: bool = True
                while player.is_alive() and enemy.is_alive():

                    if turn:
                        player.attack(enemy)
                    else:
                        enemy.attack(player)
                    
                    turn = self.change_turn(turn)

                    self.print_combatants(player, enemy)

                    if player.is_dead():
                        print("VOCÊ PERDEU O COMBATE!")
                        wait_user()
                        return
                        
            print("VOCÊ VENCEU O COMBATE! PARABÉNS!")
            wait_user()

    def any_enemies_alive(self, enemies: list[Character]):
        for enemy in enemies:
            if enemy.is_alive():
                return True
        return False
        
    def print_combatants(self, player: Character, enemy: Character):
        print(player.lifebar)
        print(enemy.lifebar)
        wait_user()

    def change_turn(self, turn: bool) -> bool:
        return not turn
