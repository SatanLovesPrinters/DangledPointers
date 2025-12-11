def line(val, string):
    
    if len(string) >= 1:
        string = string[0]
    elif len(string) == 0:
        string = "*"
    res = val * string
    print(res)

def square(size, character):

    i = 0
    while i < size:
        line(size, character)
        i += 1

if __name__ == "__main__":
    square(5, "x")
    print()
    square(3, "o")