import random
import dragon

class FireDragon(dragon.Dragon):
  """Attributes:
  inherits from Dragon class
  name - name of the entity
  max_hp - maximum health points of the entity
  hp - current health points of the entity
  f_shots - number of fire shots remaining

  functions:
  special attack - fire shot that does random damage between 5-9
  str - returns a string with the entity's name and hp/max_hp and remaining fire shots
  """
  
  def __init__(self, name, max_hp, f_shots):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp
    self.f_shots = f_shots

  def special_attack(self, hero):
    if self.f_shots > 0:
      damage = random.randint(5, 9)
      hero.take_damage(damage)
      self.f_shots -= 1
      return f"{self.name} engulfs you in flames for {damage} damage!"
    else:
      return f"{self.name} has no fire shots left!"

  def __str__(self):
    return f"{self.name}: {self.hp}/{self.max_hp}\nFire Shots remaining: {self.f_shots}"