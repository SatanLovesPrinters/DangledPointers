currentList = []

while True:
    item = int(input("New item: "))
    
    if item == 0:
        print("Bye!")
        break
    elif item != 0:
        currentList.append(item)
        orderedList = sorted(currentList)
        print(f"The list now: {currentList}")
        print(f"The list in order: {orderedList}")