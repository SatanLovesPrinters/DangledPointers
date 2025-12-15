# https://programming-25.mooc.fi/part-4
# Create separate functions
# --- WIP --- 
# 1 for taking input
# 2 pass the input into other functions for practice
# 3 use the main block for compiling each of the functions together

def getInput():
    strInput = input("Please type in a palindrome: ")        
    strValue = strInput
    return strValue

def palindromes(strValue):
    
    strValue = getInput()
    print(strValue)


if __name__ == "__main__":

    pass