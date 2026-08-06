filename=input("Enter the first name:")
with open(filename,"r")as f:
    lines=f.readlines()
for line in lines:
    if "11" in line:
        print(line.strip())

