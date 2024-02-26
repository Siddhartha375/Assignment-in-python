row=int(input("Enter the number of row:"))
for i in range(row):
    print(" "*(row-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(row-i-1))