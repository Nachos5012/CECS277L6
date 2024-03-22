import random
import entity


class Hero(entity.Entity):
  """Attributes:
  inherits from Entity class
  
  functions:
  sword attack - deals random damage in the range 2D6
  arrow attack - deals random damage in the range 1D12
  """

  def sword_attack(self, dragon):
    damage = (random.randint(1, 6) + random.randint(1, 6))
    dragon.take_damage(damage)
    return f"You slash the {dragon.name} with your sword for {damage} damage."

  def arrow_attack(self, dragon):
    damage = random.randint(1, 12)
    dragon.take_damage(damage)
    return f"You hit the {dragon.name} with an arrow for {damage} damage."
