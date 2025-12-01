# https://programming-25.mooc.fi/part-3

# Iteration variables: init > condition > update
a = int(input("Type in a number: "))        #initilization 
while a < 10:                               #condition
    print(a)                                
    a += 1                                  #updating variable
print("Done")

# prints even numbers 2 to 30
start = 2
end = 30
while start <= 30:
    print(start)
    start += 2

# prints out all integer numbers greater than zero but smaller than the input.
limit = int(input("Limit: "))
count = 1 

while count < limit:
    print(count)
    count += 1

# powers of 2

limit = int(input("Upper limit: "))
powVal = 1 

while powVal <= limit:
    print(powVal)
    powVal *= 2

# powers of base n 

limit = int(input("Upper limit: "))         # WATCH OUT: Missing ')' will KO the while () / cause unexpected syntax errors later in code
base = int(input("Base: "))

val = 1

while val <= limit:
    print(val)
    val *= base

# Sum of consecutive numbers v1
# i.e. Limit 2: (1 + 2 = 3) | Limit of 10: (1 + 2 + 3 + 4 = 10) | Limit of 18: ...

limit = int(input("Limit: "))
sumTotal = 0
counter = 0

while sumTotal < limit:
    counter += 1
    sumTotal += counter

print(sumTotal)

# sum of consecutive numbers, v2.0
# Limit of 2: (1 + 2 = 3) | Limit of 10: (1 + 2 + 3 + 4 = 10)

limit = int(input("Limit: "))
sumTotal = 0
counter = 0
wordOutput = ""

while sumTotal < limit:
    counter += 1
    sumTotal += counter

    wordOutput += str(counter)
    if sumTotal < limit:        # if we hit the last item in the list, don't add the plus
        wordOutput += " + "
            

print(f"The consecutive sum: {wordOutput} = {sumTotal}")

#make a pyramid

n = 10
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1 

# multiply string
strHiya = input("Please type in a string: ")
num = int(input("Please type in an amount: "))
print(strHiya * num)

# Learning about len()

input_string = input("Please type in a string: ")
print(input_string)
print("-" * len(input_string))

# len() exercise

message1 = input("Please type in string 1: ")
message2 = input("Please type in string 2: ")

if len(message1) > len(message2):
    print(f"{message1} is longer")
elif len(message1) < len(message2):
    print(f"{message2} is longer")
else:
    print("The strings are equally long")