import random

#Variable Initializing
world = []
terrain = ["w","w","w","g","g","g","g","g","g","g"]
chunkrange = [8,17,26,35,44,53,62,71]
terraincovered = random.choice(terrain)

#Chunk Generating
for i in range(81):
    world.append(random.choice(terrain))

world[40] = "O"

#Game Loop
while True:
    playerlocation = world.index("O")
    
    for i in range(81):
        if i in chunkrange:
            print(world[i])
        else:
            print(world[i],end="")
            
    playerinput = input("\n")
    
    if playerinput == "w":
        world[playerlocation] = terraincovered
        terraincovered = world[playerlocation-9]
        world[playerlocation-9] = "O"
        
    if playerinput == "s":
        world[playerlocation] = terraincovered
        terraincovered = world[playerlocation+9]
        world[playerlocation+9] = "O"
   
    if playerinput == "a":
        world[playerlocation] = terraincovered
        terraincovered = world[playerlocation-1]
        world[playerlocation-1] = "O"
        
    if playerinput == "d":
        world[playerlocation] = terraincovered
        terraincovered = world[playerlocation+1]
        world[playerlocation+1] = "O"