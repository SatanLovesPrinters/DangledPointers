def no_vowels(my_string):
    new_string = ""
    vowels = 'aeiou'
    for letter in my_string:
        if letter not in vowels:
            new_string += letter
    return new_string