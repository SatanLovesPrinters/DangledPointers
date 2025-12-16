# Length of the longest

def length_of_longest(strList):
    maxFind = 0
    for x in strList:
        if len(x) > maxFind:
            maxFind = len(x)
    return maxFind