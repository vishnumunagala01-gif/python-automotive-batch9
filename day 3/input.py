print("max \n min \n swap")
a,b = map(int,input("enter the numbers").split())
choice=int(input("enter the num"))
if(choice==1):
    print(max(a,b))
elif(choice==2):
    print(min(a,b))
elif(choice==3):
    a,b=b,a
    print("swap is %d %d" %(a,b))
else:
    print("invalid input")