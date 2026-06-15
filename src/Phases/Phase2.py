from src.Engine.Phase import Phase
from src.Engine.Combat import Combat
from src.Character.Character import Character

from src.Character.Role.Warrior import Warrior
from src.Character.Role.Mage import Mage
from src.Character.Role.Assassin import Assassin

from src.utils.terminal import clear_terminal
from src.utils.time import delay
 
class Phase2(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        clear_terminal()

        print("Fase 2 rodando")
        delay()

        Combat().run(player, [Character(Assassin(), "Zed"), Character(Mage(), "Ryze")])
