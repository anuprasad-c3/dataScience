list1=input("Enter elements of first list separeted by space :").split()
list2=input("Enter elements of second list separeted by space :").split()
common=False
for item in list1:
    if item in list2:
        common=True
        break
print("Have common member :",common)
