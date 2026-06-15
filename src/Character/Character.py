from __future__ import annotations

from random import randint
from src.Character.Lifebar import Lifebar
from src.utils.time import delay

from src.utils.terminal import *

class CharacterStatusDTO():
        
    def __init__(self):
        self.health_points: int     = 0
        self.max_health_points: int = 0

        self.attack_damage: int     = 0
        self.magic_damage: int      = 0
        self.physical_defense: int  = 0
        self.magic_defense: int     = 0
        self.critical_rate: int     = 0

class Character():

    def __init__(self, role: "Role", name:str = ""):

        self.health_points: int
        self.max_health_points: int

        self.attack_damage: int
        self.magic_damage: int
        self.physical_defense: int
        self.magic_defense: int
        self.critical_rate: int

        self.name:str = name
        self.role: "Role" = role

        Status: CharacterStatusDTO = self.role.get_base_status()
        self.apply_status(Status)

        self.level: int = 1
        self.lifebar: Lifebar = Lifebar(self)

        self.playable: bool = False


    def apply_status(self, Status: CharacterStatusDTO) -> None:
        self.health_points     = Status.health_points
        self.max_health_points = Status.max_health_points
        self.attack_damage     = Status.attack_damage
        self.magic_damage      = Status.magic_damage
        self.physical_defense  = Status.physical_defense
        self.magic_defense     = Status.magic_defense
        self.critical_rate     = Status.critical_rate

    def attack(self, target: "Character"):
        damage: int = self.calculate_damage(self.attack_damage, target.physical_defense)
        print(f"{self.name} IRÁ ATACAR {set_color_red()}{target.name}{set_color_white()}")
        delay(500)

        if self.attackWillCrit():
            damage *= 2
            print(f"{set_color_yellow()}ATAQUE CRÍTICO!{set_color_white()}")
            delay(500)
        target.receive_damage(damage)
        delay(500)

    def receive_damage(self, damage: int):
        print(f"{self.name} recebeu {set_color_red()}{damage}{set_color_white()} de dano")
        self.health_points = max(0, self.health_points - damage)
        self.lifebar.update(self)
    
    def calculate_damage(self, damage: int, defense: int) -> int:
        return round(damage * 100 / (100+defense))

    def attackWillCrit(self):
        return self.critical_rate > randint(0, 99)
    
    def cure(self, heal: int):
        if heal + self.health_points > self.max_health_points:
            self.health_points = self.max_health_points
            return
        
        self.health_points += heal
        print(f"{self.name} curou {set_color_green()}{heal}{set_color_white()} pontos d evida")
        delay()
    
    def is_alive(self):
        return self.health_points > 0
    
    def is_dead(self):
        return not self.is_alive()
    
    def set_playable(self):
        self.playable = True

    def level_up(self, level_counter: int = 1):
        status: CharacterStatusDTO = self.role.get_level_progression()

        health_increment = self.health_points / self.max_health_points

        self.max_health_points += status.max_health_points * level_counter
        self.attack_damage += status.attack_damage * level_counter
        self.magic_damage += status.magic_damage * level_counter
        self.physical_defense += status.physical_defense * level_counter
        self.magic_defense += status.magic_defense * level_counter

        self.health_points = int(health_increment * self.max_health_points)

        self.level += level_counter
    
    def __str__(self):
        return f"{self.name} - {self.level} | {self.health_points}/{self.max_health_points}"