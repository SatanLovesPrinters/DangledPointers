def anagrams(strVal1, strVal2):
    sortedList1 = sorted(strVal1)
    sortedList2 = sorted(strVal2)
    if sortedList1 == sortedList2:
        return True
    else:
        return False