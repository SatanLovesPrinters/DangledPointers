def line(val, string):
    
    if len(string) >= 1:
        string = string[0]
    elif len(string) == 0:
        string = "*"
    res = val * string
    print(res)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")

