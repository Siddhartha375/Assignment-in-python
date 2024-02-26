with open("content.txt") as f:
    data=f.read()

with open("copy.txt",'w') as f:
    f.write(data)   