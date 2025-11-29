# https://programming-25.mooc.fi/part-1
# getting started

print (":-)")

greeting = "Hello there!"

# minutes in a year 
minutes = 60
hours_in_day = 24
days_in_year = 365

minutes_in_day = minutes * hours_in_day
minutes_in_year = minutes_in_day * days_in_year

print (f"{greeting}")
print (f"Minutes in 1 day: {minutes_in_day}")
print(f"Minutes in 1 year: {minutes_in_year}")

# intro to input

input_name = input("What is your name?: ")
input_email = input("What is your email address?: ")
input_nickname = input("What is your nickname?: ")

print("Let's confirm the details!")
print(f"Your name: {input_name}")
print(f"Your email address: {input_email}")
print(f"Your nickname: {input_nickname}")

input_name = input("What is your name again?: ")
print(f"Ah right! Your name is: {input_name}")

# Story Example

story_name = input("What is the story-be-tolder's name?: ")
story_year = input("What year does this story take place?: ")
story_general = input("Explain the story!: ")
story_complete = print(f"The story begins with {story_name} on a warm day in the year {story_year}. {story_general}")

# arithmetic operations
#strings
result = 10 * 25
print(result)

print("The result is: " + str(result))
print (f"The result is (w/ f-strings): {result}")

x = 27
y = 15
valueSum = x + y
valueSub = x - y
valueMult = x * y
valueDiv = x / y

print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")

#convert-to-single line with  print(arg, end="")

input_str = input("Where year were you born?: ")
year = int(input_str)
print(f"Your age at the end of the year 2025: {2025 - year}")
print(f"Your age at the end of the year 2055: {2055 - year}")

#String Adjustments

name = input("What is your name? ")
year = int(input("Year of birth? "))
output = print(f"Hi {name}, you will be {2021 - year} years old at the end of the year 2021")

#increase variable count

sum = 0 
sum += int(input("First number: "))
sum += int(input("Second number: "))
sum += int(input("Third number: "))
print (f"The sum of the numbers is: {sum}")


# exercise
# write program > asks  user for > number of days. 
# prints out number of seconds in the amount of days given.

days_input = int(input("How many days? (converted to seconds): "))
minutes_in_day = 60 * 24
seconds_in_day = minutes_in_day * 60
days_to_seconds = seconds_in_day * days_input
print(f"Seconds in that many days: {days_to_seconds}")

# Determine students on course

students_on_course = int(input("How many students on the course?"))
group_size = int(input("Desired group size? "))

if group_size % 2 == 0:
    groups_formed = students_on_course // group_size
if group_size % 2 != 0:
    groups_formed = (students_on_course // group_size) + 1

print(f"Number of groups formed: {groups_formed}")

#Soup w/ Jerry
name_JerryCheck = input("Please tell me your name: ")
cost = 5.90

if name_JerryCheck == 'Jerry':
    print("Next please!")
if name_JerryCheck != 'Jerry':
    soupPortion = int(input("How many portions of soup? "))
    
    print(f"The total cost is {cost * soupPortion}")
    print("Next please!")


#string determined operations

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
opReq = str(input("Operation: "))

if opReq == 'add':
    print(f"{num1} + {num2} = {num1 + num2}")
if opReq == 'subtraction':
    print(f"{num1} - {num2} = {num1 - num2}")
if opReq == 'multiply':
    print(f"{num1} * {num2} = {num1 * num2}")
if opReq == 'division':
    print(f"{num1} / {num2} = {num1 / num2}")

# Temp Conversion
inputTemp = int(input("Please type in a temperature (F): "))
tempF_to_C = ((inputTemp - 32) / (9/5))

if tempF_to_C < 0:
    print(f"{inputTemp} degrees Fahrenheit equals {tempF_to_C} degrees Celsius ")
    print("Brr! It's cold in here!")

if tempF_to_C >= 0:
    print(f"{inputTemp} degrees Fahrenheit equals {tempF_to_C} degrees Celsius ")

### Closing Section (Part 1) ###

from math import sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

# solve ax^2 + bx + c 

x_pos = (-b + (sqrt(b**2 - (4*a*c))))/(2*a)
x_neg = (-b - (sqrt(b**2 - (4*a*c))))/(2*a)
print (f"The roots are {x_pos} and {x_neg}")
