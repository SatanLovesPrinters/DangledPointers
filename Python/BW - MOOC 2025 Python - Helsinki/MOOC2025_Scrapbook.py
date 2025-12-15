# https://programming-25.mooc.fi/part-4
# --- WIP ---
# - Determine how lists pop & remove at certain indexes.
# - This currently finds the first instance of x & pops it/removes it. Causing issues with unordered lists. 
# - Need to make stronger determination on pop vs remove

def sum_of_positives(intList):

    for x in intList:
        i = 1
        if x < 0:
            intList.pop(i)
            i +=1
        else:
            i += 1
            continue  
    return sum(intList)      
        

my_list = [-9, -7, -5, -2, 0, 1, 3, 5, 7, 5]
result = sum_of_positives(my_list)
print("The result is", result)

