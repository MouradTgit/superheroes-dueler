import random
from hero import Hero  
class Team:
  def __init__(self, name):
    '''Initialize your team with its team name and an empty list of heroes'''
    self.name = name
    self.heroes = []

  def add_hero(self, hero):
    '''Add Hero object to self.heroes.'''
    self.heroes.append(hero)

  def remove_hero(self, name):
    '''Remove hero from heroes list.
    If Hero isn't found return 0.
    '''
    for hero in self.heroes:
      if hero.name == name:
        self.heroes.remove(hero)
        return 1  # found + removed
    return 0  # not found

  def view_all_heroes(self):
    '''Prints out all heroes to the console.'''
    for hero in self.heroes:
      print(hero.name)

  def stats(self):
    '''Print team statistics'''
    for hero in self.heroes:
      if hero.deaths == 0:
        kd = hero.kills 
      else:
        kd = hero.kills / hero.deaths
      print(f"{hero.name} Kill/Deaths:{kd}")

  def revive_heroes(self):
    '''Reset all heroes health to startng_health'''
    for hero in self.heroes:
      hero.current_health = hero.starting_health

  def attack(self, other_team):
    '''Battle each team against each other.'''
    living_heroes = self.heroes[:]
    living_opponents = other_team.heroes[:]

    while len(living_heroes) > 0 and len(living_opponents) > 0:
      hero = random.choice(living_heroes)
      opponent = random.choice(living_opponents)

      hero.fight(opponent)

      # remove dead heroes from living lists
      living_heroes = [h for h in living_heroes if h.is_alive()]
      living_opponents = [h for h in living_opponents if h.is_alive()]


if __name__ == "__main__":
  team = Team("Justice League")
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  team.add_hero(hero1)
  team.add_hero(hero2)

  team.view_all_heroes()
  print(team.remove_hero("Dumbledore"))  # 1
  print(team.remove_hero("Batman"))      # 0
  team.view_all_heroes()