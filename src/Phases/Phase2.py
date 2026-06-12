from src.Engine.Phase import Phase
from src.Character.Character import Character
from src.Character.Role.Warrior import Warrior
from src.Character.Role.Mage import Mage

from src.Engine.Combat import Combat

 
class Phase2(Phase):
    def __init__(self):
        pass

    def run(self, player: Character):
        print("Fase 2 rodando")

        Combat().run(player, [Character(Mage(), "Gandalf")])
