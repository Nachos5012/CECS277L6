# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 03/05/2024
# Module 6 - Dragon Trainer
# Purpose - create a game where the user has to defeat 3 dragons

import dragon
import fire_dragon
import flying_dragon
import hero
import entity
import check_input
import random


def main():
  """main function"""
  name = input("What is your name, challenger?\n")
  print(f"Welcome to dragon training, {name}!\nYou must defeat 3 dragons.\n")
  #hero
  hero_obj = hero.Hero(name, 50)
  #dragons
  dragon_list = [
      dragon.Dragon("Deadly Nadder", 10),
      fire_dragon.FireDragon("Gronckle", 15, 3),
      flying_dragon.FlyingDragon("Timberjack", 20, 5)
  ]
  #while loop
  while len(dragon_list) > 0 and hero_obj.hp > 0:
    print(hero_obj)
    for i in range(len(dragon_list)):
      print(f"{i+1}. {dragon_list[i]}")
    dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1,
                                              len(dragon_list))
    print("\nAttack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")
    weapon_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
    print()
    if weapon_choice == 1:
      if dragon_choice == 1:
        print(hero_obj.arrow_attack(dragon_list[0]))
      elif dragon_choice == 2:
        print(hero_obj.arrow_attack(dragon_list[1]))
      elif dragon_choice == 3:
        print(hero_obj.arrow_attack(dragon_list[2]))
    if weapon_choice == 2:
      if dragon_choice == 1:
        print(hero_obj.sword_attack(dragon_list[0]))
      elif dragon_choice == 2:
        print(hero_obj.sword_attack(dragon_list[1]))
      elif dragon_choice == 3:
        print(hero_obj.sword_attack(dragon_list[2]))
    if dragon_list[dragon_choice - 1].hp == 0:
      print(f"You have slain the {dragon_list[dragon_choice-1].name}")
      dragon_list.remove(dragon_list[dragon_choice - 1])
    if len(dragon_list) > 0:
      dragon_attacker = random.randint(1, len(dragon_list))
      dragon_attack = random.randint(1, 2)
      if dragon_attack == 1:
        print(dragon_list[dragon_attacker - 1].basic_attack(hero_obj))
      elif dragon_attack == 2:
        print(dragon_list[dragon_attacker - 1].special_attack(hero_obj))
    print()
  if hero_obj.hp == 0:
    print("You have been defeated!")
  else:
    print(
        "Congratulations! You have defeated all 3 dragons, you have passed the trials."
    )


main()
