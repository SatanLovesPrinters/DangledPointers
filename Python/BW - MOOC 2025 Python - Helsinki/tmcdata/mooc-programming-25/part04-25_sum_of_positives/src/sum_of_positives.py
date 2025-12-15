def sum_of_positives(intList):

    for x in intList[::-1]:
        if x <= 0:
            intList.remove(x)
    return sum(intList)
