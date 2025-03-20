import copy
import random
import time
from characters import get_char

def battle(chars): # Master function for battles.
    if len(chars) >= 2: # Checks if there are enough characters to battle
        def levelup(char): # Inner function that gives a multiplier to each player's stats depending on their level.
            char["strength"] = int(char["strength"] * char["level"])
            char["health"] = int(char["health"] * char["level"])
            char["defense"] = int(char["defense"] * char["level"])
            char["speed"] = int(char["speed"] * char["level"])
            
            int(char["health"])
            int(char["defense"])
            int(char["speed"])
            return char
        first_fighter = levelup(copy.deepcopy(get_char(chars, "battle", "'s the first character"))) # Gets the characters to be battled
        second_fighter = levelup(copy.deepcopy(get_char(chars, "battle", "'s the second character")))
        if second_fighter["speed"] > first_fighter["speed"]: # Sorts the fighters by their speed, so that it can decide who goes first.
            temp = second_fighter
            second_fighter = first_fighter
            first_fighter = temp
        print(f'{second_fighter["name"]} tried to attack, but {first_fighter["name"]} was too quick!')
        
        while True: # Main battle loop
            firsts_attack = random.randint(first_fighter["strength"] - 10, first_fighter["strength"] + 10) # Selects a damage that the first attack will do with a bit of randomness.
            print(f'{first_fighter["name"]} attacked {second_fighter["name"]} with a damage of {firsts_attack}!')
            time.sleep(2)
            
            seconds_defense = random.randint(second_fighter["defense"] - 10, second_fighter["defense"] + 10) # Selects a defense that the second fighter is able to block, with some randomness.
            if seconds_defense < 0: # Makes sure that the fighter's defense is not negative.
                seconds_defense = 0
            if firsts_attack - seconds_defense > 0: # Subtracts the attack minus the defense from the second attacker's health.
                second_fighter["health"] -= (firsts_attack - seconds_defense)
            if second_fighter["health"] < 0: # Makes sure that the fighter's health is not displayed as negative.
                second_fighter["health"] = 0
            print(f"{second_fighter['name']} was able to block {seconds_defense} damage of {first_fighter['name']}'s attack. {second_fighter['name']} now has {second_fighter['health']} health.")
            time.sleep(2)
            
            if second_fighter["health"] == 0: # If the second fighter is dead, announce the winner and level them up.
                for char in chars:
                    if char['name'] == first_fighter['name']:
                        char["level"] += 0.2
                print(f'{first_fighter["name"]} has defeated {second_fighter["name"]}, and has leveled up! Congratulations!')
                return chars
            
            temp = second_fighter # Swaps the first and second fighter, which lets the second fighter attack.
            second_fighter = first_fighter
            first_fighter = temp
    else:
        print("There aren't enough characters to battle.")
        return chars