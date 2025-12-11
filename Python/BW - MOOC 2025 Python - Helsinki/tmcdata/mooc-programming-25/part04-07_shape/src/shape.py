def line(val, string):
    
    if len(string) >= 1:
        string = string[0]
    elif len(string) == 0:
        string = "*"
    res = val * string
    print(res)

def triangle(size, string):
    
    i = 0
    while i <= size:
        line(i, string)
        i += 1

def rectangle(val1, val2, string): #length, width, char to use

    i = 0
    j = 0 
    rowMax = val2       # width

    while i < val1:  
        while j < rowMax:     # length
            line(val1, string)
            j += 1
        break

def shape(val1, string, val2, fillerString):
    
    triangle(val1, string)
    rectangle(val1, val2, fillerString)

if __name__ == "__main__":
    shape(5, "x", 2, "o")
    