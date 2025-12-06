# https://programming-25.mooc.fi/part-3
# WIP | Figure out string continuation (Limit is determined, using python logic to keep printing until the limit is met is not known as of now. )

def squared(text, times):
    rowLimit = times          #how many spaces we can take up
    boxLimit = times**2       #repeat text until all spaces taken up
    
    if len(text) < rowLimit:
        ...


if __name__ == "__main__":
    squared("ab", 3)