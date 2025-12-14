# https://programming-25.mooc.fi/part-4

values = []

while True:
    i = 0 
    inputChoice = input("a(d)d, (r)emove, e(x)it: ")
    if inputChoice == 'd': #add
        values.append(1+i)
        i += 1
        print(f"The list is now {values}")
    elif inputChoice == 'r': #remove
        values.remove(1-i)
        i -= 1
        print(f"The list is now {values}")
    elif inputChoice == 'x': #exit
        print("Bye!")
        break
