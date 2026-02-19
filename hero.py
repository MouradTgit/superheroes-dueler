import random
# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def fight(self, opponent):
    winner = random.choice([self, opponent])

    print(winner.name + "Wins!")
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner,
  # Hint: Look into random library, more specifically the choice method

class Ability:
  def __init__(self, name, max_damage):
    self.name = name
    # Assign the "name" and "max_damage"
    # for a specific instance of the Ability class
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    random_value = random.randint(0,self.max_damage)
    return random_value

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    
    
    hero1.fight(hero2)

    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
  