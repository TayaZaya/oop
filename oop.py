
#Given the below class:
import self as self

"""
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

tobby = Cat('Tobby', 20)
maggie = Cat('Maggie', 15)
luna = Cat('Luna', 10)

print(cat1)
print(cat2)
print(cat3)

def Oldest_Cat(*args):
    return max(args)
    return Cat(args)

print(f"The oldest cat is {Oldest_Cat(tobby.age, maggie.age, luna.age)} years old.")

"""
# 1 Instantiate the Cat object with 3 cats#

# 2 Create a function that finds the oldest cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2


class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


my_cats = [Cat("Tobby", 2),Cat("Simon", 5),Cat("Luna", 12)]

my_pets = Pets(my_cats)

my_pets.walk()

#1 Add nother Cat

#2 Create a list of all of the pets (create 3 cat instances from the above)

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance

