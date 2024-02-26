#def factorial(n):
   # product=1
   # for i in range(n):
  #      product=product*(i+1)
 #   return product
#f=factorial(5)
#print(f)
      #OR

def factorial_Recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_Recursive(n-1)
f=factorial_Recursive(4)
print(f)