#! /usr/bin/env python3
"""
This is a code that includes creating, (and most importantly) slaying animals
for fun. Viewer discretion is advised.

The first function called "genesis" uses a template and randomly chooses
from choices given to it, thus creating a bunch of animals.

The second function called "armagedon" drowns animals according to
a death rate that is given to it.

The third function called "hunter" uses a hunter as a tool to massacre
certain animals with 50% accuracy.

Author's note: Enjoy!
"""

import random

amount = 20
animals = []


def genesis(amount):
    while len(animals) < amount:
        animal = {"amount_of_legs": 0, "fur": 0, "diet": 0}         # template
        animal["amount_of_legs"] = random.choice([2, 3, 4])
        animal["fur"] = random.choice([True, False])
        animal["diet"] = random.choice(["meat", "vegie", "both"])
        animals.append(animal)

# The function above replaces values 0 for each key randomly and gradually
# creates the required amount of animals.


genesis(amount)

print("{} animals were created.".format(len(animals)))

death_rate = 70
survivors = []


def armagedon(animals, death_rate, survivors):
    for x in animals:
        a = random.randrange(1, 101)
        if a > death_rate:
            survivors.append(x)

# The function above randomly generates a number "a" that cannot be
# larger than 100. The larger the "death_rate" is, the smaller is the
# probability of the generated number "a" being larger.
# That means that if "death_rate" = 100, the probability
# of animals' survival is 0%.


armagedon(animals, death_rate, survivors)

print("{} animals survived the armagedon.".format(len(survivors)))

accuracy = 50


def hunter(animals, accuracy):
    for animal in animals:
        a = random.randrange(1, 101)
        if a > accuracy:
            pass
        elif animal["amount_of_legs"] == 2:
            animal.clear()
        elif animal["fur"]:
            animal.clear()
        elif animal["diet"] == "meat":
            animal.clear()
    while {} in animals:
        animals.remove({})

# The function above works the same as the one called "armagedon".
# It randomly generates a number "a" that cannot be
# higher than 100. The larger the "accuracy" is, the smaller is the
# probability of the generated number "a" being larger.
# In case the number "a" is smaller that "accuracy" and at least
# one of the next conditions is met, the dictionary is cleared.
# At the end, all empty dictionaries in "animals" are removed.


hunter(animals, accuracy)

print("{} animals survived the madness of a certain hunter."
      .format(len(animals)))
