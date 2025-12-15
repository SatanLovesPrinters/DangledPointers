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