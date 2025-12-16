def formatted(floatNumList):

    modifiedList = []
    for floater in floatNumList:
        results = f"{floater:.2f}"
        modifiedList.append(results)
    return modifiedList