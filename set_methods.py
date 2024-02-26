# Creating an empty sets.
a=set()
print(type(a))
# Adding values to an empty set
a.add(3)
a.add(3)
a.add(2)
a.add(5)
a.add((1,2,1,2))
 #a.add([2,3,2]) # Not  allowed list inside the sets
#a.add({3:4}) # Not allowed dictionary inside the sets
print(a)
print(len(a)) # print the length of the sets
# Removal of an Items.
a.remove(5) # remove 5 from set a
print(a)
# Delete a random element from the sets
print(a.pop())
print(a)


