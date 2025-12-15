def even_numbers(intList):
    newList = []
    for x in intList[::-1]:
        if x % 2 == 0:
            newList.append(x)
    return sorted(newList)
