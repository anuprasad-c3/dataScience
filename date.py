date1=input("Enter the first date: ").split()
date2=input("Enter the second date: ").split()
day1=int(date1[0])
month1=int(date1[1])
year1=int(date1[2])
day2=int(date2[0])
month2=int(date2[1])
year2=int(date2[2])
d1=(year1,month1,date1)
d2=(year2,month2,date2)
if d1<d2:
    print("The first date is earlier.")
else:
    print("Both dates are the same.")
