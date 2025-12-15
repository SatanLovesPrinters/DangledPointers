### https://programming-25.mooc.fi/part-4
### Start Date:         12/10/2025
### Completion Date:    -
### Review / POW:
### - Iterating on a specific condition | Escaping on a specific index (Resolved with Discord review on Modulo %)
### - 
### - 


# Quick intro on string conversion
# Utilize dir() for help in the python console

def SimpleSomethingModulo(high, low):
    a = high
    b = low
    
    while b <= a:
        message = f"A mod B: {a} % {b} = {a % b} || B mod A: {b} % {a} = {b % a}"    
        print(message)
        b += 1
        lineSep = len(message) * "-"
    
    print(lineSep)
 
def spruce(size):
    print("a spruce!")
    
    i = 1
    treeLimit = size*2

    while (i % treeLimit) >= 0:
        spacerTotal = (treeLimit - i)
        spacerStringHalf = (spacerTotal//2)*' ' 
        posVal = i % treeLimit
        if posVal % 2 == 1:
            treeLimbs = (i * "*")
            print(spacerStringHalf + treeLimbs + spacerStringHalf)
            i += 1
        elif (i % treeLimit) == 0:
            i = 1
            spacerTotal = (treeLimit - i)
            spacerStringHalf = (spacerTotal//2)*' '
            print(spacerStringHalf + "*" + spacerStringHalf)
            break
        else:
            i+= 1

def my_sum(a, b):
    return a + b

def smallest(a, b):
    if a < b:
        return a
    return b

def difference(a, b):

    return a-b

def maxVal1(a, b):
    if a > b:
        return a
    else:
        return b

def maxVal2(a, b):
    if a > b:
        print(a)
    else:
        print(b)

def ask_for_name():
    name = input("What is your name?: ")
    return name

def greatestVal(a, b, c):
    if a >= b >= c or a >= c >= b:
        return a
    elif b >= a >= c or b >= c >= a:
        return b
    elif c >= a >= b or c >= b >= a:
        return c
        
def same_chars(text, val1, val2):
    
    arrayMax = len(text)

    if val1 > arrayMax or val2 >= arrayMax:
        return False
    elif text[val1] == text[val2]:
        return True
    else:
        return False

def first_word(text):
    
    sentenceList = text.split()
    return sentenceList[0]

def second_word(text):

    sentenceList = text.split()
    return sentenceList[1]
   
def last_word(text):
 
    sentenceList = text.split()
    return sentenceList[-1]

# the instructor solution uses a count & then passes the count into each function. Super creative. 
# I switched to using lists because it seemed easier than tracking the empty spaces.

def instructor_find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
    	if str[index] == " ":
    	    counter += 1
    	    if counter == whatth:
    	        break
    	    word = ""
    	else:
    	    word += str[index]
    	index += 1
    return word
 
def instructor_first_word(mjono):
    return instructor_find_word(mjono, 1)
 
def instructor_second_word(mjono):
    return instructor_find_word(mjono, 2)
 
def instructor_last_word(mjono):
    return instructor_find_word(mjono, 0)

if __name__ == "__main__":
    spruce(5)
    SimpleSomethingModulo(10, 1)
    SimpleSomethingModulo(6, 1)


#Lists Exercises
my_list: int = list[int]
seconds_list: int = list[int]

my_list = [1,2,3,4,5]
seconds_list = []

while True:
    index = int(input("Determine the list: "))

    if index == -1:
        break
    
    elif index == 1:
        newVal = int(input("New value: "))
        my_list.append(newVal)
        print(my_list) 
    
    elif index == 2:     
        newVal = int(input("New value: "))
        seconds_list.append(newVal)
        print(seconds_list)

    elif index == -1:
        break
    
    else:
        print(f"My List: {my_list} | Seconds list: {seconds_list}")

#Lists Exercises
values = []
i = 1

while True:
    
    print(f"The list is now {values}")
    inputChoice = input("a(d)d, (r)emove, e(x)it: ")
    if inputChoice == 'd': #add
        values.append(i)
        i += 1
    elif inputChoice == 'r': #remove
        i -= 1
        values.remove(i)
    elif inputChoice == 'x': #exit
        break

print("Bye!")    

# Same word twice exercise 
counter = 0
words = []

while True:
    word = input("Word: ")
    if word not in words:
        words.append(word)
        counter += 1
    elif word in words:
        print(f"You typed in {counter} different words")
        break


# List / Ordered List
currentList = []

while True:
    item = int(input("New item: "))
    
    if item == 0:
        print("Bye!")
        break
    elif item != 0:
        currentList.append(item)
        orderedList = sorted(currentList)
        print(f"The list now: {currentList}")
        print(f"The list in order: {orderedList}")

# Back to functions!

def length(x):
    return len(x)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)

# Arithmetic mean
def mean(my_list : int):
    result = sum(my_list) / len(my_list)
    return result

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)

# Range
def range_of_list(my_list : list):
    greatest = max(my_list)
    smallest = min(my_list)
    rangeVal = greatest - smallest
    return rangeVal

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)

# List integers from - to + 

valinput = int(input("Please type in a positive integer: "))

for i in range(-(valinput),valinput+1):
    if i == 0:
        i += 1
    else:
        print(i)
        i += 1
# Creates ... you guessed it... a list of stars
def list_of_stars(intList):
    for intVal in intList:
        print(intVal * "*")
if __name__ == "__main__":
    list_of_stars([3,7,1,1,2])

#anagrams
def anagrams(strVal1, strVal2):
    sortedList1 = sorted(strVal1)
    sortedList2 = sorted(strVal2)
    if sortedList1 == sortedList2:
        return True
    else:
        return False
#anagrams one liner
def instructor_anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False

#Functioning Palindromes (attempt to not use __main__ v1)
def getStringInput():
    strInput = input("Please type in a palindrome: ")        
    strValue = strInput
    return strValue

def palindromes(word):
    
    if word == word[::-1]:
        return True
    elif word != word[::-1]:
        return False
    
def main():

    while True:
        word = input("Please type in a palindrome: ")
        palindromes(word)

        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break
        elif palindromes(word) == False:
            print("that wasn't a palindrome")
            
main() #<---------------Took an hour to notice what had happened. Even though the if code block had been omitted. 
# This is still needed to  call the function in.