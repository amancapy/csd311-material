import random

class Cat:
    def __init__(self, breed, age, cuteness, parent=None):
        self.breed = breed
        self.age = age
        self.cuteness = cuteness
        self.parent = parent

    def __eq__(self, other):
        return [self.breed, self.age, self.cuteness] == [other.breed, other.age, other.cuteness]
    
    def __gt__(self, other):
        return self.age > other.age
    

cat = Cat("tabby", 5, 100_000)
cats_kitten = Cat("orange tabby", 1, 1000_000, parent=cat)

cats_kitten.parent.cuteness += 900_000


a_bunch_of_cats = [Cat("tabby", random.randint(3, 15), random.randint(10000, 1000000000), parent=None) for _ in range(100)]
a_bunch_of_cats.sort()
print(a_bunch_of_cats) # [<__main__.Cat object at 0x7efdb6004910>, <__main__.Cat object at 0x7efdb60051d0>, <__main__.Cat object at 0x7ef ... ]

# what

# go back and def __repr__(self) for class Cat
"""
class Cat:
    ...
    def __repr__(self):
        return f"({self.breed}, {self.age}, {self.cuteness})"
"""

print(a_bunch_of_cats) # [("tabby", 3, 928310486), ("tabby", 3, 669073172), ("tabby", 3, 201969569), ("tabby", 3, 939196711), ("tabby", 3, 617045230), ("tabby", 3, 235358942), ("tabby", 3, 500763847), ("tabby", 3, 215745443), (4, 8474..) ... ]


def pet_cat(cat):
    return "hi kitty :D"

cats_i_have_pet = set()

for new_cat in a_bunch_of_cats:
    if new_cat not in cats_i_have_pet: # Error: Cat is not a hashable type :(
        pet_cat(new_cat)
        cats_i_have_pet.add(new_cat) # same error :(((

# go back and def __hash__(self) for class Cat
"""
class Cat:
    ...
    def __hash__(self):
            return hash((self.age, self.cuteness)) # internal magic :)
"""

# pet every cat :D