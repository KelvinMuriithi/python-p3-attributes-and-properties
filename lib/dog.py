#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Fido", breed="Beagle"):
        self.name = name
        self.breed = breed

    # name property
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # breed property
    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

dog1 = Dog("Max", "Beagle")
# Output: Setting name to Max
#         Setting breed to Beagle

dog2 = Dog("Buddy", "Dragon Dog")
# Output: Setting name to Buddy
#         Breed must be in list of approved breeds.

print(dog1.breed)
