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

# length - 1 = lasts in list

input_string = input("Please type in a string: ")
index = 0
counter = 0

while index < len(input_string):
    if len(input_string) > 0:
        print(input_string[counter-1])
        counter -= 1
        index += 1
    else:
        print("The input string is empty. There is no first character")
        break

# Grid of hashes

width = int(input("Width: "))
height = int(input("Height: "))

symbol = "#"

while height > 0: 
    print(symbol * width)
    height -= 1

# Underlining

input_string = input("Please type in a string: ")
empty = ''
symbol = '-'

while input_string != empty:
       print(input_string)
       print(len(input_string)*symbol)
       input_string = input("Please type in a string: ")

# Right-aligned with 20 characters

string_input = input("Please type in a string: ")
char_limit = 20
symbol_limit = char_limit - len(string_input)
symbol_input = symbol_limit * '*'

if len(string_input) < char_limit:
    print(f"{symbol_input}{string_input}")

# frame a word

word = input("Word: ")
char_limit = 30
char_symbol = '*'

filler_space = int(char_limit - len(word) -2)//2 #total space, subtract our word, divide that for each side of empty space : -2 for 1* on each side. 
filler_string = ' ' * filler_space

border = char_limit * char_symbol

custom_row_odd = f"*{filler_string}{word}{filler_string} *"
custom_row_even = f"*{filler_string}{word}{filler_string}*"

if len(word) % 2 == 0:
    print(border)
    print(custom_row_even)
    print(border)

elif len(word) % 2 != 0:
    print(border)
    print(custom_row_odd)
    print(border)

# splicing, substrings
input_string = "XeroxTheMightyWingDinger"
print(input_string[0:3])
print(input_string[4:10])
print(input_string[:3])
print(input_string[4:])
print(input_string[::-1])

#substrings part 1
input_string = input("Please type in a string: ")
index = 0

while index < len(input_string):
    index += 1
    print(input_string[0:index])

#substrings part 2
input_string = input("Please type in a string: ")
limit = len(input_string)
index = 0
counter_index = 0


while index < len(input_string): # For TEST: While 0 < 4
    counter_index -= 1             #counterIndex = -1
    print(input_string[counter_index:limit]) 
    index += 1

# searching slices

input_string = "test"

print("t" in input_string)     ## True
print("x" in input_string)     ## False
print("es" in input_string)    ## True
print("ets" in input_string)   ## False

# searching substrings/slices example

input_string = "perpendicular"
while True:
    substring = input("What are you looking for (eg: Perpendicular): ")
    if substring in input_string:
        print("Found it")
    else:
        print("Not found")

# vowel check v2.0 

input_string = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]

    if vowel in input_string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index += 1

# use of find()

input_string = "test"

print(input_string.find("t")) # 0 (at [0]) note this is finding the next occurrence, not all  
print(input_string.find('x')) # -1 (-1 = not found)
print(input_string.find("es")) # 1 (at [1])
print(input_string.find("ets")) # -1 (not found)


# iterating a substring search

input_string = "perpendicular"

while True:
    substring = input("What are you looking for?: ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")

# find the character & print the next 2 values after it (if none, exits program)
word = input("Please type in a word: ")
index = 0

while index < len(word): 
    substring = input("Please type in a character: ")
    index = word.find(substring) #jump to the character place we want
    if index + 2 > len(word):
        break
    elif index + 2 < len(word):
        print(word[index:index+3])
        break
    else:
        break

# find all sub strings (Joined the Python discord & spent ~6 hours working through this syntax)

word = input("Word: ")
substring = input("What are you looking for? ")

index = word.find(substring)

while index >= 0 and (index + 2 < len(word)):              
    
    print(word[index:index+3])
    index += 1
    index = word.find(substring,index)

# find 2nd occurrences 

string_input = input("Please type in a string: ")       #Input a string
substring = input("Please type in a substring: ")       #Input substring
index = string_input.find(substring)                    #Index starts at the first occurrence of requested substring
counter = 1

while index >= 0:                                       #While substring is found
    
    if counter < 2:
        counter += 1
        index += 1
        index = string_input.find(substring,index+len(substring))   #find (in word) the (substring,from substring location + substring length)
       
    elif counter == 2:
        print(f"The second occurrence of the substring is at index {index}.")
        break

if index == -1:
    print("The substring does not occur twice in the string.")

# More about loops!

number = int(input("Please type in a number: "))

while number > 0:
    i = 0 
    while i < number:
        print(f"{i} ", end="")
        i += 1
    print("")
    number -=1

# Print a multiplication table for the number
number = int(input("Please type in a number: "))
xVal = 1

while xVal <= number:
    yVal = 1
    while yVal < number:
        print(f"{xVal} x {yVal} = {xVal*yVal}")
        yVal += 1
    print(f"{xVal} x {yVal} = {xVal*yVal}")
    xVal += 1

#first letter of words (non-book approach)

sentence = "Humpty Dumpty sat on a wall" 
words = sentence.split()

for letter in words:
    if letter:
        print(letter[0])

    #first letter of words (nested loop approach)

sentence_input = input("Please type in a sentence") # "Ran to the store" 
sentence_input = " " + sentence_input               # " Ran to the store"                Add a space to the start for handling purposes

    #Setup starting index. 
index = 1
while index < len(sentence):
    if sentence_input[index-1] == " " and sentence_input[index] != " ":         #If the spot before is a blank space (which at start is due to above)
        print(sentence_input[index])                                            #and if the current spot is a letter, then print out the current letter 
    index +=1

#Factorials
while True:
    number = int(input("Number: "))

    if number < 0:
        print("Thanks and bye!")
        break
    elif number == 1:
        print(f"The factorial of the number {number} is {number}")
    elif number > 0:                           
        counter = number - 1                #counter = 5 - 1
        val_stored = number * 1             #Start the count from 1
    
        while counter != 0:
            val_stored = val_stored * counter   #val_stored = 20 : val_stored * next increment (3)
            counter -= 1                        # repeat: val_stored = 60*2
    
        print(f"The factorial of the number {number} is {val_stored}")

#Overkilled Flipped Pairs
#i.e. 5 = 2 1 4 3 5 | 1 (start) 2 3 4 5

number = int(input("Please type in a number: "))

startVal = 1
nextVal = startVal+1
tempVal = 1
counter = 1 

while counter <= number:
        
    if counter == number and tempVal == counter:
        print(tempVal)
        break
    elif counter == number and tempVal > counter:
        print(number)
        break
    elif startVal < nextVal:
        print(nextVal)
        tempVal = startVal
        counter += 1
        startVal += 1
    elif startVal > tempVal:
        print(tempVal)
        startVal += 1
        tempVal = startVal
        nextVal = startVal+1
        counter += 1

# Instructor Solution to Flip_the_Pairs: (NB: Note bene)
number = int(input("Please type in a number: "))
   
index = 1
while index+1 <= number:
    print(index+1)
    print(index)
    index += 2

if index <= number:
    print (index)

#Alternating pairs by the limit set
number = int(input("Please type in a number: "))
   
index = 1
tempVal = number

while index <= number:
   if index > tempVal:
       break
   elif index == tempVal:
       print(tempVal)
       break
   print(index)
   print(tempVal)
   index += 1
   tempVal -= 1
    
def first_character(text):  #functions should always called at the top of the code, these are listed for section notes when transferred out of the scrapbook/testing zone.  
    print(text[0], text[2:3])

def squared(x):
    print(f"The square of the number {x} is {x*x}")

def sum(x, y):
    result = x+y
    print(f"The sum of the arguments {x} and {y} is {result}")

def mean(x, y, z):
    result = (x+y+z)/3
    print(result)

# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

    squared(2)
    squared(5)

    x = 100
    y = 30
    sum(1,2)
    sum(x + y,10)
    mean(5, 2, 1)

#Print_Many_Times 
def print_many_times(text, times):
    text = f"{text}\n"
    result = text * times
    print(result)

if __name__ == "__main__":
    print_many_times("python", 5)

    #Solution / Instructor Submitted Solution (NB: Note Bene)

def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1

#square of hashes function

def hash_square(length):
    column = 0
    symbol = "#"
    row_result = symbol * length

    while column < length:
        print(row_result)
        column += 1

if __name__ == "__main__":
    hash_square(5)

#Create a chessboard based on the specified length
def chessboard(length):
    row = length
    column = length
    index = 0
    column_index = 0

    while column_index < length: 
        index = 0

        if column_index % 2 == 0:
            print(1, end="")
            index += 1

            while index < length:
            
             if index % 2 == 0:
                print(1, end="")
             else:
                print(0, end="")
             index += 1

        elif column_index % 2 != 0:
            print(0, end="")
            
            while index < length-1:
            
             if index % 2 == 0:
                print(1, end="")
             else:
                print(0, end="")
             index += 1        
        
        print()
        column_index += 1
        
            
if __name__ == "__main__":
    chessboard(6)

###Instructor solution to chessboard
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1