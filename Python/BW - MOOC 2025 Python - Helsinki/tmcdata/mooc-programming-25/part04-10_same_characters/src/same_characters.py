def same_chars(text, val1, val2):
    
    arrayMax = len(text)

    if val1 > arrayMax or val2 >= arrayMax:
        return False
    elif text[val1] == text[val2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))