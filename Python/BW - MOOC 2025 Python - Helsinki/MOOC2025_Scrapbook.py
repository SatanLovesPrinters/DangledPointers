# https://programming-25.mooc.fi/part-4

def even_numbers(intList):
    newList = []
    for x in intList[::-1]:
        if x % 2 == 0:
            newList.append(x)
    return sorted(newList)

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)