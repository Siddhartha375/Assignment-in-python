# use open() to read the file
f=open("Sample.txt",'r') # by defult the mode is 'r'
#data=f.read()
data=f.read(5) # print the first 5 characters from the file
print(data)
f.close()
