words=["dog",'cat','rat']
with open("problem_05.txt") as f:
    data=f.read()

    for word in words:
        data=data.replace(word,"@#$%^&")

with open("problem_05.txt",'w') as f:
    f.write(data) 