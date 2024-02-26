#5!=1x2x3x4x5
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(f"factorial of {n} is={fact}")
