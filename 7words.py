with open("C:/Users/Caden/Desktop/sevenwords.txt",'r') as file:
    for line in file:
        line = line.strip()
        if line.count(" ") != 6:
            print("ERROR: \""+line+"\" does not equal seven words!")
        else:
            print(line)