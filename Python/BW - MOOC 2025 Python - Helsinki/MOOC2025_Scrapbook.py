# https://programming-25.mooc.fi/part-3

#WIP - Enter a number - Swap each pair of numbers so they appear flipped.
#i.e. 5 = 2 1 4 3 5 

while True:
    number = int(input("please type in a number"))
    xVal = 0
    yVal = 0
    counter = 1
    

    if number < 0:                                  #5 !< 0, continues
        break

    while index <= number:

        if index <= number_temp:
            print(counter+1)
            index += 1
        elif index > number_temp:
            print(index)
            number_temp = index
            index += 1
    
    