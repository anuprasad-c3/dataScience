class Bank:
    def __init__(self):
        self.acc_no=0
        self.bal=0
        print(self.bal)

    def addbank(self):
        self.acc_no=int(input("Enter the bank account number :"))

    def deposit(self):
        amt=int(input("Enter amount for deposit :"))
        self.bal=self.bal+amt
        print("Amount deposited!")

    def withdraw(self):
        amt=int(input("Enter amount for withdraw :"))
        self.bal=self.bal-amt
        print("\n Amount withdrawed !")

    def trasfer(self):
        print("tranfer")

    def balance(self):
        print("total Balance :",self.bal)

b=Bank()
ch=-1;

while(ch!=0):
    print("1.Add Bank Account")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.tranfer")
    print("5.show balance")
    print("0.Exit")

    ch=int(input("Enter your choice :"))
    if(ch==1):
        b.addbank()
    if(ch==2):
        b.deposit()
    if(ch==3):
        b.withdraw()
    if(ch==4):
        b.tranfer()
    if(ch==5):
        b.balance()

