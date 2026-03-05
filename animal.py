# animal.py

class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating")

  def drink(self):
    print(f"{self.name} is drinking")


class Frog(Animal):
  def jump(self):
    print(f"{self.name} is jumping")


if __name__ == "__main__":
  a = Animal("Bunny")
  f = Frog("Freddy")

  a.eat()
  a.drink()

  f.eat()
  f.drink()
  f.jump()