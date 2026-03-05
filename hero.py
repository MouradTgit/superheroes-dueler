from armor import Armor
from ability import Ability
import random
from weapon import Weapon

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
    self.deaths = 0
    self.kills = 0

  def add_ability(self,ability):
    self.abilities.append(ability)

  def attack(self):
    '''Calculate the total damage from all ability attacks.
      return: total_damage:Int
    '''
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

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
    if len(self.abilities) == 0 and len(opponent.abilities) == 0:
      print("Draw")
      return

    while self.is_alive() and opponent.is_alive():
      opponent.take_damage(self.attack())
      if not opponent.is_alive():
        self.add_kill(1)
        opponent.add_death(1)
        print(f"{self.name} won!")
        return

      self.take_damage(opponent.attack())
      if not self.is_alive():
        opponent.add_kill(1)
        self.add_death(1)
        print(f"{opponent.name} won!")
        return
  
  def add_weapon(self, weapon):
    '''Add weapon to self.abilities'''
    self.abilities.append(weapon)

  def add_kill(self, num_kills):
    '''Update self.kills by num_kills amount'''
    self.kills += num_kills

  def add_death(self, num_deaths):
    '''Update deaths with num_deaths'''
    self.deaths += num_deaths

    
  

if __name__ == "__main__":
  hero = Hero("Wonder Woman")
  weapon = Weapon("Lasso of Truth", 90)
  hero.add_weapon(weapon)
  print(hero.attack())