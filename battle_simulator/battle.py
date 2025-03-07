import copy
import random
import time
from characters import get_char

def battle(chars):
    if len(chars) >= 2:
        first_fighter = copy.deepcopy(get_char(chars, "battle", "'s the first character"))
        second_fighter = copy.deepcopy(get_char(chars, "battle", "'s the second character"))
        if second_fighter["speed"] > first_fighter["speed"]:
            temp = second_fighter
            second_fighter = first_fighter
            first_fighter = temp
        while True:
            firsts_attack = random.randint(first_fighter["strength"] - 10, first_fighter["strength"] + 10)
            print(f'{first_fighter["name"]} attacked {second_fighter["name"]} with a damage of {firsts_attack}!')
            time.sleep(0.5)
            if firsts_attack - second_fighter["defense"] < 0:
                pass
            print(f"{second_fighter['name']} was able to block {second_fighter['defense']} damage of {first_fighter['name']}'s attack. {second_fighter['name']} now has {second_fighter['health']} health.")
    else:
        print("There aren't enough characters to battle.")

battle([])