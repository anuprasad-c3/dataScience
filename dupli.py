items = input("Enter elements seperated by space :").split()
uni = []
for item in items:
    if item not in uni:
        uni.append(item)
print("List after removing duplicates :",uni)
