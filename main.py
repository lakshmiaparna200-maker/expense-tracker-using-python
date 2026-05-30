def add_expense():
    item=(input("enter expense name:"))
    amount=(int(input("enter amount:")))
    file=open("expense.txt","a")
    file.write(item +" "+ str(amount)+ "\n")
    file.close()
    print("expense added...")
def view_expense():
    file=open("expense.txt","r")
    data=(file.read())
    if data=="":
     print("EXPENSES ARE NOT ADDED..")
    else:
     print(data)
    file.close()
def total_expense():
    file=open("expense.txt","r")
    total=0
    for line in file:
        data=line.strip().split(" ")
        amount=int(data[1])
        total=total+amount
    print("total expense:",total)
    file.close()
while True:
    print("_________expense tracker__________")
    print("1.add expense")
    print("2.view expense")
    print("3.total expense")
    print("4.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        add_expense()
    elif choice==2:
        view_expense()
    elif choice==3:
        total_expense()
    elif choice==4:
        print("exiting...")
        break
    else:
        print("invalid choice..")