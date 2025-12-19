from range import *  # taking everything from the range.py
p=int(input("enter the principle amount : "))
t=int(input("enter the time period : "))
r=float(input("enter the rate of intrest :"))

#si=ptr/100
pt=cal(p,t,3)    # 3 represents multiplicaction
ptr=cal(pt,r,3)
si=cal(ptr,100,4)   # 4 represents division
print(f"the simple intrest is : {si}")
      