def sumofnatural(n):
    if n==0 :
        return 0
    return n+sumofnatural(n-1)
s=sumofnatural(1)
print(s)