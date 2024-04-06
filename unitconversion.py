# Inch to MM = 1 to 25.4

while True:    
    numbers = [round(float(i.strip()) / 5,3) for i in input().split("x")]
    print(*numbers, sep=' x ')