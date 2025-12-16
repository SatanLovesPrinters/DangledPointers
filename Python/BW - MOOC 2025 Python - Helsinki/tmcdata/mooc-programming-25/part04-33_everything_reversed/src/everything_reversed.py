def everything_reversed(strList):
    newList = []
    for strings in strList:
        newList.insert(0,strings[::-1])
    return (newList)
