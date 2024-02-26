with open("problem_04.txt")as f:
    data=f.read()
data=data.replace("motherchod","#$@%^&")

with open("problem_04.txt",'w') as f:
    f.write(data)
    