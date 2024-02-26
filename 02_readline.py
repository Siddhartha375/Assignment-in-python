f=open("Sample.txt",'r')
data=f.readline() # read 1st line
print(data)
data=f.readline() # read 2nd line and so on
print(data)
f.close()