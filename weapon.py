# weapon.py
import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    """Return a random int between half max_damage and max_damage."""
    half = self.max_damage // 2
    return random.randint(half, self.max_damage)