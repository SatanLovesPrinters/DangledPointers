def solution(s:str):
    sNew = []
    filler = ["_"]
    results = []
    sNew = s.split()
    incr = 2
    together = []
    i = 0

    if len(s) % 2 == 1:
        combined = sNew + filler
        together = "".join(combined)

        while i < len(together):
            results.append(together[i:i+2])
            i+=2
        return results

    elif len(s) % 2 == 0:
        while i < len(s):
            results.append(s[i:i + 2])
            i += 2
        return results
    else:
        return 0

print(solution('abc'))
print(solution('abcdef'))