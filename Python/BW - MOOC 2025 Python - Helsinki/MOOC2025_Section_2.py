# https://programming-25.mooc.fi/part-2
## Terminology

name = "I am a printer!"
age = 18

if name == "I am a printer!": #Conditional Statement
    print("Go away printer!")            #Print Statement
    number = 2              #Assignment Statement

if age > 17: 
                            #Start of conditional block
    print(f"You are of age!: {age}")
    age += 1
    print(f"You are now one year older (Age: {age})")
                            #End of conditional block

print("This is a separate block")

# Type identifier

print(type("Name")) # class str
print(type(100))    # class int
print(type(100.0))  # class float


# typecasting

temperature = float(input("Please type in a number: "))
intValue = int(temperature)
decValue = temperature - intValue

print(f"Integer part: {intValue}")
print(f"Decimal part: {decValue}")

# if, else, elif

number = int(input("Please type in a number: "))

if number < 0:
    print("The number is negative")
else:
    print("The number is positive or zero")

if number % 2 == 0:
    print("The number is even.")
else:                       
    print("The number is odd.")

#elif in use

goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("Home team is victorious!")
elif goals_away > goals_home:
    print("Away team is victorious!")
else:
    print("It's a tie!")


person1_name = input("Name: ")
person1_age = int(input("Age: "))

person2_name = input("Name: ")
person2_age = int(input("Age: "))

if person1_age > person2_age:
    print(f"The elder is {person1_name}")
elif person2_age > person1_age:
    print(f"The elder is {person2_name}")
else:
    print(f"{person1_name} and {person2_name} are the same age")

#elif age check

age = int(input("What is your age? "))

if age >= 5:
    print(f"Ok, you're {age} years old")
elif 0 <= age < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# if, elif, else

name = str(input("Please type in your name: "))

if name == 'Morty' or name == 'Ferdie':
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == 'Huey' or name == 'Dewey' or name == 'Louie':
    print("I think you might be one of Donald Duck's nephews.")
else:
    print("You're not a nephew of any character I know of.")

points = int(input("How many points [0-100]: "))

# if, elif, else | Combining and chaining conditions

if points < 0 or points > 100:
    print("impossible!")
elif 0 <= points <= 49:
    print("Grade: fail")
elif 50 <= points <= 59:
    print("Grade: 1")
elif 60 <= points <= 69:
    print("Grade: 2")
elif 70 <= points <= 79:
    print("Grade: 3")
elif 80 <= points <= 89:
    print("Grade: 4")
elif 90 <= points <= 100:
    print("Grade: 5")

# if, elif, else | Combining and chaining conditions

divInput = int(input("Number: "))

if divInput % 3 == 0 and divInput % 5 == 0:
    print("FizzBuzz")
elif divInput % 3 == 0:
    print("Fizz")
elif divInput % 5 == 0:
    print("Buzz")

# Leap year | Evaluating to true & then checking:

year = int(input("Please type in a year: "))

if (year % 4 == 0) and (year % 100 != 0): #year is divisible by 4 but not 100 
    print("That year is a leap year!")
elif (year % 100 == 0) and (year % 400 != 0): #year is divisible by 100 but not 400
    print("That year is not a leap year.")
elif (year % 400 == 0):  # year is divisible by 400 
   print("That year is a leap year.")
else:
    print("That year is not a leap year.")

# Alphabetically in the middle (no lists/no sort function)

a = str(input("1st letter: "))
b = str(input("2nd letter: "))
c = str(input("3rd letter: "))

if a < b < c:
    print(f"The letter in the middle is {b}")
elif c < b < a:
    print(f"The letter in the middle is {b}")
elif b < a < c:
    print(f"The letter in the middle is {a}")
elif c < a < b:
    print(f"The letter in the middle is {a}")
elif a < c < b:
    print(f"The letter in the middle is {c}")
elif b < c < a:
    print(f"The letter in the middle is {c}")

#calculate amount of tax based on gift amount from close relative

giftValue = float(input("Value of gift: "))

if giftValue < 5000:
    print("No tax!")
elif 5000 <= giftValue < 25000:
    tax_flat = 100
    tax_rate = .08
    tax_lower_limit = 5000
    tax_Owed = tax_flat + (giftValue - tax_lower_limit) * tax_rate
    print(f"Amount of tax: {tax_Owed} euros")
elif 25000 <= giftValue < 55000:
    tax_flat = 1700
    tax_rate = .10
    tax_lower_limit = 25000
    tax_Owed = tax_flat + (giftValue - tax_lower_limit) * tax_rate
    print(f"Amount of tax: {tax_Owed} euros")
elif 55000 <= giftValue < 200000:
    tax_flat = 4700
    tax_rate = .12
    tax_lower_limit = 55000
    tax_Owed = tax_flat + (giftValue - tax_lower_limit) * tax_rate
    print(f"Amount of tax: {tax_Owed} euros")
elif 200000 <= giftValue < 1000000:
    tax_flat = 22100
    tax_rate = .15
    tax_lower_limit = 200000
    tax_Owed = tax_flat + (giftValue - tax_lower_limit) * tax_rate
    print(f"Amount of tax: {tax_Owed} euros")
elif giftValue >= 1000000:
    tax_flat = 142100
    tax_rate = .17
    tax_lower_limit = 1000000
    tax_Owed = tax_flat + (giftValue - tax_lower_limit) * tax_rate
    print(f"Amount of tax: {tax_Owed} euros")

# Simple loops (Part2-Ch4)

while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break
    print(number ** 2)

print("Thanks and bye!")


# PIN Check (basic)
while True:
    code = int(input("Please type in your PIN: "))
    if code == 1234:
        break
    print("Incorrect - Try again.")

print("Correct PIN entered!")

# Shall we continue?
while True:
    print("hi")
    userInput = input("Shall we continue?")
    if userInput == "no":
        break
        
print("okay then")

#Password bool check
password = input("Password: ")
passwordConfirmed = False

while passwordConfirmed == False:
    passwordConfirmation = input("Repeat password: ")

    if password == passwordConfirmation:
        passwordConfirmed = True
    else:
        print("They do not match!")

print("User account created!")

#Pin Check 

pin_set = 4321
pin_guess = False
pin_counter = 0

while pin_guess == False:
    
    pin_check = int(input("PIN: "))
    
    if pin_check == pin_set and pin_counter == 0:
        print(f"Correct! It only took you one single attempt!")
        pin_guess = True
    elif pin_check == pin_set and pin_counter > 0:
        pin_counter += 1
        print(f"Correct! It took you {pin_counter} attempts")
        pin_guess = True
    elif pin_check != pin_set:
        print("Wrong")
        pin_counter += 1

# enter a year, determine if it's a leap year & then print out the next leap year (Took ~4-5 hours & the results were not optimal, failed & resulted in finding the solution)
# key takeaways: break, while True, simplifying the issue
# the firstValue was always going to be set, to avoid this immediately increment the input by 1 & then start looking for the next leap year. 

year_start = int(input("Year: "))
year = year_start + 1

while True:
    if year % 100 == 0: # divis by 100 
        if year % 400 == 0: #divis by 100 and 400 = leapyear
            break       #if year is found, stop the loop (?)
    elif year % 4 == 0: # only divis by 4 = leap year, stop the loop
        break
 
    year += 1
 
print(f"The next leap year after {year_start} is {year}")

#enter words, exit on end or double entered word. print out story
prev_word = ""
story_sentence = ""

while True:
    story_input = str(input("Please type in a word: "))
      
    if story_input == 'end' or story_input == prev_word:
        break
    else:
        prev_word = story_input
        story_sentence += story_input + " "
    
print(f"{story_sentence}")

# asks user for integers until 0 is entered

numbers_list = ""
numbers_counter = 0
numbers_sum = 0
numbers_sum_total = 0
numbers_mean = 0
numbers_pos_count = 0
numbers_neg_count = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:  

    numbers_input = int(input("Number: "))

    if numbers_input == 0:
        break
    if numbers_input > 0:
        numbers_pos_count += 1   
    if numbers_input < 0:
        numbers_neg_count += 1
   
    numbers_counter += 1                #add to count
    numbers_sum = numbers_input    #convert input to integers 
    numbers_sum_total += numbers_sum    #add the sum to the previous sum
    numbers_mean = numbers_sum_total / numbers_counter

if numbers_input == 0:
    print(f"Numbers typed in {numbers_counter}")
    print(f"The sum of the numbers is {numbers_sum_total}")
    print(f"The mean of the numbers is {numbers_mean}")
    print(f"Positive numbers {numbers_pos_count}")
    print(f"Negative numbers {numbers_neg_count}")

