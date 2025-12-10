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