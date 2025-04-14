#Classes and objects notes

"""
What is a class in python?
- A class is a blueprint for creating an object.

What is an object in python?
- Every instance of a class is an object.

How do python classes relate to python objects?
- Objects are made inside of classes.

How do you create a python class?
- Run 'class name:' and 'name' will be the class name. You do have to define __init__ with the proper variables.

What are methods?
- A function that is specific to a class.

How do you create a python object?
- Use the class to run 'name = class(param)' and name will be your object, with parameters defined by __init__. You can then run name.property and it will give you the property.

How to you call a method for an object?
- Run 'object.method(param)'

Why do we use python classes?
- It organizes your information better, so it's more convenient to access and modify. Simplifies later code.
"""

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHealth: {self.hp}\nDamage: {self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} damage and {opponent.name} now has {opponent.hp} health!")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} damage and {self.name} now has {self.hp} health!")
                if self.hp <= 0:
                    print(f"{self.name} has been knocked out. {opponent.name} won the battle!")
            else:
                print(f"{opponent.name} has been knocked out. {self.name} won the battle!")


bob = pokemon("Mr.Bob", "Charizard", 300, 95)
fluffy = pokemon("Fluffy", "Arcanine", 280, 110)

bob.battle(fluffy)
print(fluffy)