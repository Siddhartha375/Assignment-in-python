with open('another.txt','r') as f: # it is the syntax
    a=f.read()
    # no need to f.close()
with open('another.txt','w') as f:
    a=f.write("I am write")
    print(a)
