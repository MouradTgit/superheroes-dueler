from armor import Armor
from ability import Ability
import random
# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
    '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def add_ability(self,ability):
    self.abilities.append(ability)

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage
    '''Calculate the total damage from all ability attacks.
      return: total_damage:Int
  '''

  def add_armor(self, armor):
    '''Add armor to self.armors
      Armor: Armor Object
    '''
    self.armors.append(armor)

  def defend(self):
    '''Calculate the total block amount from all armor blocks.
       return: total_block:Int
    '''
    # If hero is "dead", they can't defend
    if self.current_health <= 0:
      return 0

    total_block = 0
    for armor in self.armors:
      total_block += armor.block()
    return total_block

  def take_damage(self, damage):
    '''Updates self.current_health to reflect the damage minus the defense.'''
    defense = self.defend()
    final_damage = damage - defense

    # stretch goal: don't allow "negative damage" to heal you
    if final_damage < 0:
      final_damage = 0

    self.current_health -= final_damage

  def is_alive(self):
    '''Return True or False depending on whether the hero is alive or not.'''
    return self.current_health > 0

  def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.'''
    # 0) check if at least one hero has abilities
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print("Draw")
      return

    # 1) fighting loop
    while self.is_alive() and opponent.is_alive():
      # self attacks opponent
      damage_to_opponent = self.attack()
      opponent.take_damage(damage_to_opponent)

      # check if opponent died
      if not opponent.is_alive():
        print(f"{self.name} won!")
        return

      # opponent attacks self
      damage_to_self = opponent.attack()
      self.take_damage(damage_to_self)

      # check if self died
      if not self.is_alive():
        print(f"{opponent.name} won!")
        return

  

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)