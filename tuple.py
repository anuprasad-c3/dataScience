pairs = input("Enter key-value pairs seperated by spaces :",).split()
t = [(pairs[i],pairs[i+1]) for i in range(0,len(pairs),2)]
d=dict(t)
print("Dictionary :",d)
