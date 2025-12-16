def distinct_numbers(intList):
    
    uniqueList = []
    i = 0 
    for num in intList:
        if num not in uniqueList:
            uniqueList.append(num)
    return sorted(uniqueList)