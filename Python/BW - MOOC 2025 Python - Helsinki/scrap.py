def square_digits(num):
    #9119 = 81-1-1-81
    #{9**2}-{1**2}-{1**2}-{9**2} 

    digits = [int(digit) for digit in str(num)]
    squaredList = []
    result = []

    for digit in digits:
        squaredList.append(digit**2)
        result = str(squaredList)
    for element in squaredList:
        "-".join(element)

    return squaredList

print(square_digits(9119))