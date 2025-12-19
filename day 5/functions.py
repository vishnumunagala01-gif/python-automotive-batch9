n=int(input("enter the first number:"))
m=int(input("enter the second number:"))
def cal(a,b):
    choice=int(input("enter the choice:"))
    if (choice==1):
        return a+b
    elif(choice==2):
        return a-b
    elif(choice==3):
        return a*b
    elif(choice==4):
        return a/b
    else:
        return "wrong input"
print(cal(n,m))

