myDic={"fast":"This is fast.",
       "sidd":"A codder.",
       "harry":"A joaker.",
       "marks":[4,3,2],
       "another":{'Sidd':'Fuck'}
}
print(myDic.keys())#prints the keys the dictionary
print(list(myDic.keys())) #convert keys into a list

print(myDic.values()) # print the keys values in a list

print(myDic.items()) # print the(key,values) for all contents of the dictionary
print(myDic)

updateDic={  #updates the dictionary by adding key-values pairs from updateDic
    "New":"This is new dictionary",
    "harry":"a dancer" # value changed from haary =a joaker to a dancer
}
myDic.update(updateDic)
print(myDic)

print(myDic.get("harry"))
