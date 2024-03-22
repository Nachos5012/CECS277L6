import random
import dragon

class FlyingDragon(dragon.Dragon):
  """Attributes:
  inherits from Dragon class
  name - name of the entity
  max_hp - maximum health points of the entity
  hp - current health points of the entity
  swoops - number of swoop attacks remaining

  functions:
  special attack - swoop attack that does random damage between 5-9
  str - returns a string with the entity's name and hp/max_hp and remaining swoop attacks
  """
  def __init__(self, name, max_hp, swoops):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp
    self.swoops = swoops

  def special_attack(self, hero):
    if self.swoops > 0:
      damage = random.randint(5, 9)
      hero.take_damage(damage)
      self.swoops -= 1
      return f"{self.name} swoop attacks you for {damage} damage!"
    else:
      return f"{self.name} has no swoop attacks left!"

  def __str__(self):
    return f"{self.name}: {self.hp}/{self.max_hp}\nSwoop attacks remaining: {self.swoops}"