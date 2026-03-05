# arena.py
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: Team
        team_two: Team
    '''
    self.team_one = Team("Team One")
    self.team_two = Team("Team Two")

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = int(input("What is the max damage of the ability?  "))
    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    name = input("What is the weapon name?  ")
    max_damage = int(input("What is the max damage of the weapon?  "))
    return Weapon(name, max_damage)

  def create_armor(self):
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    name = input("What is the armor name?  ")
    max_block = int(input("What is the max block of the armor?  "))
    return Armor(name, max_block)

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)

    add_item = None
    while add_item != "4":
      add_item = input(
        "[1] Add ability\n"
        "[2] Add weapon\n"
        "[3] Add armor\n"
        "[4] Done adding items\n\n"
        "Your choice: "
      )

      if add_item == "1":
        ability = self.create_ability()
        hero.add_ability(ability)

      elif add_item == "2":
        weapon = self.create_weapon()
        hero.add_weapon(weapon)

      elif add_item == "3":
        armor = self.create_armor()
        hero.add_armor(armor)

    return hero

  def build_team_one(self):
    '''Prompt the user to build team_one '''
    self.team_one.name = input("Team One name: ")
    num = int(input("How many members would you like on Team One?\n"))
    for _ in range(num):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  def build_team_two(self):
    '''Prompt the user to build team_two'''
    self.team_two.name = input("Team Two name: ")
    num = int(input("How many members would you like on Team Two?\n"))
    for _ in range(num):
      hero = self.create_hero()
      self.team_two.add_hero(hero)

  def team_battle(self):
    '''Battle team_one and team_two together.'''
    self.team_one.attack(self.team_two)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # Average K/D Team One
    team1_kills = 0
    team1_deaths = 0
    for hero in self.team_one.heroes:
      team1_kills += hero.kills
      team1_deaths += hero.deaths
    if team1_deaths == 0:
      team1_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team1_kills / team1_deaths))

    # Average K/D Team Two
    team2_kills = 0
    team2_deaths = 0
    for hero in self.team_two.heroes:
      team2_kills += hero.kills
      team2_deaths += hero.deaths
    if team2_deaths == 0:
      team2_deaths = 1
    print(self.team_two.name + " average K/D was: " + str(team2_kills / team2_deaths))

    # Surviving heroes Team One
    team1_alive = 0
    for hero in self.team_one.heroes:
      if hero.is_alive():
        team1_alive += 1
        print("survived from " + self.team_one.name + ": " + hero.name)

    # Surviving heroes Team Two
    team2_alive = 0
    for hero in self.team_two.heroes:
      if hero.is_alive():
        team2_alive += 1
        print("survived from " + self.team_two.name + ": " + hero.name)

    # Declare winning team
    if team1_alive > team2_alive:
      print("\nWinner: " + self.team_one.name)
    elif team2_alive > team1_alive:
      print("\nWinner: " + self.team_two.name)
    else:
      print("\nResult: Draw")


if __name__ == "__main__":
  game_is_running = True

  arena = Arena()
  arena.build_team_one()
  arena.build_team_two()

  while game_is_running:
    arena.team_battle()
    arena.show_stats()

    play_again = input("\nPlay Again? Y or N: ")
    if play_again.lower() == "n":
      game_is_running = False
    else:
      arena.team_one.revive_heroes()
      arena.team_two.revive_heroes()



      def sum_list(numbers):
        total = 0

        for number in numbers:
            total = total + number

        return total
      
      fruits = ["apple", "banana"]
      fruits.append("mango")

      class Dog:
        def __init__(self, name):
          self.name = name

        def bark(self)
          print("Woof!")
          
    def square(n):
      return n * n
    
    for fruit in fruits:
      print(fruit)

      class Hero:
        def __init__(self, name):
          self.name = name
          self.abilities = list()

        def add_ability(self, ability):
          self.abilities.append(ability) 
    
        def attack(self):
            total = 0

            for ability in self.abilities:
                total = total + ability

            return total
        
        class Armor:

         def __init__(self, block):
          self.block = block

         def block_damage(self):
           return self.block
         
         def largest(numbers):
           
         def largest(numbers):
           biggest = numbers[0]

           for number in numbers:
               if number > biggest:
                   biggest = number

           return biggest
         
         def is_even(n):
           return n % 2 == 0
         
         for number in range(1, 6):
             print(number)

        def defend(self):
            total = 0

            for armor in self.armors:
                total = total + armor

            return total
        
        class Shield(Armor):

         def __init__(self, block):
             super().__init__(block)

        
        def defend(self):
            total_block = 0

            for armor in self.armors:
                total_block += armor.block_damage()

            return total_block