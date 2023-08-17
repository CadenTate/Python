import math


# Functions
def solveforg(houses):
    return math.ceil(math.log(houses / 7, 2) + 2)


def getPopulation(generation):
    return (2 ** (generation + 1)) - (2 ** (generation - 2))


# Main
h = int(input("How many houses are available: "))

g = solveforg(h)
population = getPopulation(g)

print("Generation:", g)
print("Population:", population)
print("Year:", g * 25)
