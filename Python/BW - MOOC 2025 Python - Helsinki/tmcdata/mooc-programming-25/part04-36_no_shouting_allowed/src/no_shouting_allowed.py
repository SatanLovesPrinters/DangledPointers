def no_shouting(my_string):
    no_uppers = []
    for letter in my_string:
        if letter.isupper() == False:
            no_uppers.append(letter)
    return no_uppers