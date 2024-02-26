def remove_and_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

str="    This is    a   streep .    "
n=remove_and_split(str,"This")
print(n)
#print(str.strip())