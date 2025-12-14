my_list = [1,2,3,4,5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    else:     
        newVal = int(input("New value: "))
        my_list[index] = newVal
        print(my_list)

