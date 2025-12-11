def line(val, string):
    
    if len(string) >= 1:
        string = string[0]
    elif len(string) == 0:
        string = "*"
    res = val * string
    print(res)

def triangle(size):
    
    i = 0
    while i <= size:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)