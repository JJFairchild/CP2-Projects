import copy
import random
import time
from characters import get_char

#ADD LEVELS

def battle(chars):
    if len(chars) >= 2:
        first_fighter = copy.deepcopy(get_char(chars, "battle", "'s the first character"))
        second_fighter = copy.deepcopy(get_char(chars, "battle", "'s the second character"))
        if second_fighter["speed"] > first_fighter["speed"]:
            temp = second_fighter
            second_fighter = first_fighter
            first_fighter = temp
        print(f'{second_fighter["name"]} tried to attack, but {first_fighter["name"]} was too quick!')
        
        while True:
            firsts_attack = random.randint(first_fighter["strength"] - 10, first_fighter["strength"] + 10)
            print(f'{first_fighter["name"]} attacked {second_fighter["name"]} with a damage of {firsts_attack}!')
            time.sleep(2)
            
            seconds_defense = random.randint(second_fighter["defense"] - 10, second_fighter["defense"] + 10)
            if firsts_attack - seconds_defense > 0:
                second_fighter["health"] -= (firsts_attack - seconds_defense)
            if second_fighter["health"] < 0:
                second_fighter["health"] = 0
            print(f"{second_fighter['name']} was able to block {seconds_defense} damage of {first_fighter['name']}'s attack. {second_fighter['name']} now has {second_fighter['health']} health.")
            time.sleep(2)
            
            if second_fighter["health"] == 0:
                for char in chars:
                    if char['name'] == first_fighter['name']:
                        char["level"] += 0.2
                print(f"{first_fighter["name"]} has defeated {second_fighter["name"]}, and has leveled up! Congratulations!")
            
            temp = second_fighter
            second_fighter = first_fighter
            first_fighter = temp
    else:
        print("There aren't enough characters to battle.")