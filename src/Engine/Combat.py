from src.Character.Character import Character
from src.utils.inputs import wait_user, input_option

from random import randint
from src.utils.time import delay


class Combat():

    def run(self, player: Character, enemies: list[Character]) -> None:

        combat_options: list[str] = ['ATACAR']  # TODO: INSERIR OUTRAS OPÇÕES PARA O COMBATE
        
        if(len(enemies) > 1):
            print(f"{len(enemies)} INIMIGOS APARECERAM!")
        else:
            print("UM INIMIGO APARECEU!")

        delay(500)

        while player.is_alive() and self.any_enemies_alive(enemies):

            for enemy in enemies:

                self.print_combatants(player, enemy)

                turn: bool = True
                while player.is_alive() and enemy.is_alive():

                    if turn:
                        option: int = input_option(combat_options, "ESCOLHA UMA AÇÃO:")
                        delay(500)
                        self.process_action(player, option, enemy)

                    else:
                        option: int = randint(0, len(combat_options) - 1)
                        self.process_action(enemy, option, player)
                    delay(500)


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
        

    def change_turn(self, turn: bool) -> bool:
        return not turn
    
    def process_action(self, character: Character, option: int, target: Character|None)->None:

        match option:

            # ATAQUE
            case 0:
                if target == None:
                    return
                character.attack(target)
            
            # EM CASO DE ERRO -> ATAQUE
            case _:
                if target == None:
                    return
                character.attack(target)