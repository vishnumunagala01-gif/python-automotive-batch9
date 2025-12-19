#empty lists to store the values
evennum=[]
oddnum=[]
#count
even=0
odd=0
for i in range(1,11):
    n=int(input(f"enter the numbers {i}:")) #user input

    if n%2==0:
        even+=1  #incrementing count by 1
        print(f"the given {n} is even")
        evennum.append(n)
    else:
        odd+=1   #incrementing count by 1
        print(f"the given {n} is odd")
        oddnum.append(n)
print("done with 10 numbers")
print(f"even count {even}")
print(f"odd count {odd}")
print(f"evens are {evennum}")
print(f"odds are {oddnum}")