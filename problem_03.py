num=int(input("Enter the number:"))
for i in range(2,num):
    if(num%i==0):
        print(" not Prime number")
        break
else:
    print("prime")