def sum_of_positives(intList):

    for x in intList:
        
        if x < 0:
            intList.remove(x)
        else:
            sum(intList)
    return sum(intList)     

my_list = [-9, -7, -5, -2, 0, 1, 3, 5, 7, 5]
result = sum_of_positives(my_list)
print("The result is", result)