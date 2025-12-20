# values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# newValues = []
# 
# for row in values:
#     for value in row:
#         newValues.append(value)
# print(newValues)

print(*"MASH", sep="*")
print(1, 2, 3, sep="*")


rows = 3
cols = 3
rowblocks = 3
items = range(81)

for index, item in enumerate(items, start=1):
    print("_", end="")
    if index % cols == 0: print(" ", end="")
    if index % (cols*rows) == 0: print("")
    if index % (cols*rows*rowblocks) == 0: print("")