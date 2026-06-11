from src.Character.Character import Character
from src.utils.inputs import wait_user

class Combat():

    def run(self, player: Character, enemies: list[Character]) -> None:
        
        if(len(enemies) > 1):
            print(f"{len(enemies)} INIMIGOS APARECERAM!")
        else:
            print("UM INIMIGO APARECEU!")

        while player.is_alive() and self.any_enemies_alive(enemies):
            for enemy in enemies:

                print_combatants(player, enemy)
                wait_user()

                turn: bool = True
                while player.is_alive() and enemy.is_alive():

                    if turn:
                        player.attack(enemy)
                    else:
                        enemy.attack(player)    

                    print_combatants(player, enemy)
                    wait_user()

        def any_enemies_alive(enemies: list[Character]):
            for enemy in enemies:
                if enemy.is_alive():
                    return True
            return False
        
        def print_combatants(player: Character, enemy: Character):
            print(player)
            print(enemy)
            wait_user()
