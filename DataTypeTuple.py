
# Tuple is immutable that means you can't change value after assigned
# List and Tuple both are same only difference is for List we have use [] whereas for Tiple we have to use ()

val = (1, 2, "sushmi", 4, 5)
print(val)
print(type(val))
print(val[2])
print(type(val[2]))
print(type(val[0]))

dic = { "a":1, 2:"b", "manoj":"sushmi"}
print(dic)
print(type(dic))
print(dic["a"])
print(dic["manoj"])
print(dic[2])
#print(dic["b"]) - It will throw error we can't value

#Create dictionary at run time and add into it
dict={}

dict["Mridhu"]= "Manoj"
dict["Sree"]= "sushmi"
print(dict)
print(type(dict))
print(dict["Mridhu"])
print(dict["Sree"])