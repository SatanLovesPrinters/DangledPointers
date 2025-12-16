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