### https://programming-25.mooc.fi/part-4
### Start Date:         12/10/2025
### Completion Date:    -
### Review / POW:
### - 
### - 
### - Iterating on a specific condition | Escaping on a specific index


# Quick intro on string conversion
# Utilize dir() for help in the python console
while True:
    userInput = input(str("Editor: "))
    userInputConversion = userInput.lower()
    if userInputConversion == "visual studio code":
        print("an excellent choice!")
        break
    elif userInputConversion == 'emacs' or userInputConversion == 'vim' or userInputConversion == 'atom':
        print("not good")
    elif userInputConversion == 'word' or userInputConversion == 'notepad':
        print("awful")