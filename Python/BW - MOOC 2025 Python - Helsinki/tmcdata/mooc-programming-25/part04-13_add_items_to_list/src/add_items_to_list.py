item_amt = int(input("How many items: "))
items = []

while True:
    i = 1
    while i <= item_amt:
        item = int(input(f"Item {i}: "))
        items.append(item)
        i += 1
    print(items)
    break