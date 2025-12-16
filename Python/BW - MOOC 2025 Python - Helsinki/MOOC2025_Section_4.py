### https://programming-25.mooc.fi/part-4
### Start Date:         12/10/2025
### Completion Date:    12/16/2025
### Review / POW:
### - Iterating on a specific condition | Escaping on a specific index (Resolved with Discord review on Modulo %)
### - type-hinting
### - Iterating forward through a list

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


def length(x):
    return len(x)

def mean(my_list : int):
    result = sum(my_list) / len(my_list)
    return result

def range_of_list(my_list : list):
    greatest = max(my_list)
    smallest = min(my_list)
    rangeVal = greatest - smallest
    return rangeVal


    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)

def list_of_stars(intList):
    for intVal in intList:
        print(intVal * "*")
    
def anagrams(strVal1, strVal2):
    sortedList1 = sorted(strVal1)
    sortedList2 = sorted(strVal2)
    if sortedList1 == sortedList2:
        return True
    else:
        return False

def instructor_anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2) #-Anagrams one liner

#Functioning Palindromes
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
            
main() 
#<-Took an hour to notice what had happened without calling main().
# Even though the if code block had been omitted from the exercise:
# - This is still needed to  call the function in

# Unique find on sum of positives: the ability to go left to right is slight inhibited w/ lists.  
def sum_of_positives(intList):

    for x in intList[::-1]:
        if x <= 0:
            intList.remove(x)
    return sum(intList)

def even_numbers(intList):
    newList = []
    for x in intList[::-1]:
        if x % 2 == 0:
            newList.append(x)
    return sorted(newList)

def list_sum(listIntA, listIntB):
    resultsList = []
    i = 0 
    while i < len(listIntA):
        results = listIntA[i] + listIntB[i]
        resultsList.append(results)
        i += 1
    return resultsList

def distinct_numbers(intList):
    
    uniqueList = []
    i = 0 
    for num in intList:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList

def length_of_longest(strList):
    maxFind = 0
    for x in strList:
        if len(x) > maxFind:
            maxFind = len(x)
    return maxFind

def shortest(strList):
    minFind = 999
    for x in strList:
        if len(x) < minFind:
            minFind = len(x)
            minFound = x
    return minFound

def all_the_longest(strList):
    longest = ""
    longestList = []
    maxFind = 0

    for word in strList:
        if len(word) >= len(longest):
            longest = word
            maxFind = len(longest)
            longestList.append(longest)
   
        for word in longestList:
            if len(word) < maxFind:
                longestList.remove(word)
            
    return longestList

def formatted(floatNumList):

    modifiedList = []
    for floater in floatNumList:
        results = f"{floater:.2f}"
        modifiedList.append(results)
    return modifiedList

def everything_reversed(strList):
    newList = []
    for strings in strList:
        newList.insert(0,strings[::-1])
    return (newList)

def most_common_character(my_string):
    char_count_max = ""
    char_count_initial = 0
    char_count = 0
    for letter in my_string:
        char_count = my_string.count(letter)             
        if char_count > char_count_initial:
            char_count_initial = char_count
            char_count_max = letter
    return char_count_max

def no_vowels(my_string):
    new_string = ""
    vowels = 'aeiou'
    for letter in my_string:
        if letter not in vowels:
            new_string += letter
    return new_string

def no_shouting(my_string):
    no_uppers = []
    for letter in my_string:
        if letter.isupper() == False:
            no_uppers.append(letter)
    return no_uppers

def longest_series_of_neighbours(my_list):
    num_neighbors_count = 0
    num_neighbors_max = 0
    
    for num1, num2 in zip(my_list, my_list[1:]):
        if num1+1==num2 or num1-1==num2:
            num_neighbors_count += 1
            if num_neighbors_count >= num_neighbors_max:
                    num_neighbors_max = num_neighbors_count
        else:
            if num_neighbors_count >= num_neighbors_max:
                    num_neighbors_max = num_neighbors_count
            num_neighbors_count = 0
            
    return num_neighbors_max+1 # This was a cheap approach due to my approach checking each pair. 

def instructor_longest_series_of_neighbours(my_list: list): #This is the accurate approach. To find difference between two numbers use abs(a-b).
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest



names =  [ "Larry", "Jean", "Katherine", "Paul" ]
first_string = "abcdbde" # b
second_string = "exemplaryelementary" #e
my_string = "this is an example"
my_list = [3, 2, 2, 1, 3, 3, 1]
my_list_2 = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
my_list_3 = [1, 2, 3, 4]

a = [1,2,3]
b = [7,8,9]

for name in names:
    print(f"{name:15} | {name:>15}")

list_of_stars([3,7,1,1,2])
print(list_sum(a,b))
print(distinct_numbers(my_list)) # [1, 2, 3]
print(no_vowels(my_string))
print(most_common_character(first_string))
print(most_common_character(second_string))
pruned_list = no_shouting(my_list_2)
print(pruned_list)
print(longest_series_of_neighbours(my_list_3))
