from random import randint
from typing import Tuple
from time import sleep

a = 0
b = 0
c = 0
d = 0

class Player:
    def __init__(self) -> None:
        self.a = randint(1,100)
        self.b = randint(1,100)
        self.c = randint(1,100)
        self.d = randint(1,100)

    def isCorrect(self,a,b,c,d) -> bool:
        return self.a == a and self.b == b and self.c == c and self.d == d

    def parseInput(self,a:float,b:float,c:float,d:float):
        if not self.isCorrect(a,b,c,d):
            return round((self.a - a) / 10,1), round((self.b - b) / 10,1), round((self.c - c) / 10,1), round((self.d - d) / 10,1)
        else:
            return "Done"
        
player = Player()

while True:
    output = player.parseInput(a,b,c,d)

    if output == "Done":
        break

    a += output[0]
    b += output[1]
    c += output[2]
    d += output[3]

    print(a,b,c,d)
    sleep(1)