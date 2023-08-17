import itertools

numbers = [1, 2, 3, 4, 5, 6, 7]

permutations = list(itertools.permutations(numbers))

# Rule 1: Marley and Reagan must sit next to each other
seatingRule1 = []
for i in permutations:
    for k in range(2,len(i)-1):
        if i[k] == 3 and (i[k+1] == 4 or i[k-1] == 4):
            seatingRule1.append(i)

# Rule 2: Lila and Reagan must sit next to each other
seatingRule2 = []
for i in seatingRule1:
    for k in range(2,len(i)-1):
        if i[k] == 7 and (i[k+1] == 4 or i[k-1] == 4):
            seatingRule2.append(i)

# Rule 3. Judah and Polly must sit next to each other
seatingRule3 = []
for i in seatingRule2:
    for k in range(2,len(i)-1):
        if i[k] == 6 and (i[k+1] == 5 or i[k-1] == 5):
            seatingRule3.append(i)

# Rule 4. Cohen and Marly cannot sit next to each other
seatingRule4 = []
for i in seatingRule3:
    for k in range(2,len(i)-1):
        if i[k] == 3 and (i[k+1] == 2 or i[k-1] == 2):
            break
    else:
        seatingRule4.append(i)

print(seatingRule4)