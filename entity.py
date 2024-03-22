class Entity:
  """Attributes:
  name - name of the entity
  max_hp - maximum health points of the entity
  hp - current health points of the entity

  functions:
  take_damage - subtracts damage from the entity's hp
  str - returns a string with the entity's name and hp/max_hp
  """
  
  def __init__(self, name, max_hp):
    self.name = name
    self.max_hp = max_hp
    self.hp = max_hp

  def take_damage(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0

  def __str__(self):
    return f"{self.name}: {self.hp}/{self.max_hp}"
  