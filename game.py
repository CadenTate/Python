import random

#world[0] = first y level | world[0][0] = first y level and first x level | world[0][0][0] = first y and x and first  terrain
#world = [[["D"],["G"],["E"]],[["W"],["A"],["B"]],[["F"],["G"],["C"]]]
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
world = []
chunkY = -1
chunkX = -1

worldchunkY = 2
worldchunkX = 0

def chunkConverter():
    print(chunkY, chunkX)
    print(worldchunkY,worldchunkX)
    #print(world[2][0])
    print(world[worldchunkY][worldchunkX])

#chunkConverter()

def generateWorld():
    world.append(random.choice(a))
    print(world)
generateWorld()