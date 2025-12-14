values = []
i = 1

while True:
    
    print(f"The list is now {values}")
    inputChoice = input("a(d)d, (r)emove, e(x)it: ")
    if inputChoice == 'd': #add
        values.append(i)
        i += 1
    elif inputChoice == 'r': #remove
        i -= 1
        values.remove(i)
    elif inputChoice == 'x': #exit
        break

print("Bye!")    