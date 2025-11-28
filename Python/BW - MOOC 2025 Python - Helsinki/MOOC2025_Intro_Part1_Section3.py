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
