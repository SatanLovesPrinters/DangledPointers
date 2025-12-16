def shortest(strList):
    minFind = 999
    for x in strList:
        if len(x) < minFind:
            minFind = len(x)
            minFound = x
    return minFound