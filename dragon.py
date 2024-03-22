#dragon.py
import random
import entity

class Dragon(entity.Entity): 
  """Attributes:
  inherits from Entity class
  
  functions:
  basic attack - deals random damage in the range 3-7
  special attack - deals random damage in the range 4-8
  """
  
  def basic_attack(self, hero):
    """Basic Attack"""
    damage = random.randint(3,7)
    hero.take_damage(damage)
    return f"{self.name} smashes you with its tail for {damage} damage!"

  def special_attack(self, hero):
    """abstract method that each dragon will override to do a special attack"""
    damage = random.randint(4,8)
    hero.take_damage(damage)
    return f"{self.name} slashes you with its claws for {damage} damage!"
    
    