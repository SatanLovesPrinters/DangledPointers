values = []

while True:
    inputChoice = input("a(d)d, (r)emove, e(x)it")
    if inputChoice == 'd': #add
        values.append(1)
        print(f"The list is now {values}")
    elif inputChoice == 'r': #remove
        values.remove[1]
        print(f"The list is now {values}")
    elif inputChoice == 'x': #exit
        print("Bye!")
        break

# remove item