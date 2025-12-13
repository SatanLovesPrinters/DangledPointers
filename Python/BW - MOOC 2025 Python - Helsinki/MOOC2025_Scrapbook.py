# https://programming-25.mooc.fi/part-4

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
    i = 0
    word = ""
    while i < len(text):
        if text[i+1] == " ":
            word += text[i]
            return word
        else:
            word += text[i]
            i += 1

def second_word(text):

    pass 

   
def last_word(text):
    pass



if __name__ == "__main__":
    
    sentence = "duty sworn to was"
    print(first_word(sentence))
    print(second_word(sentence))
