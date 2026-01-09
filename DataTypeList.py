values=[1, 2, "mridhu", 4, 5]
#List is data type that allows multiple values and can be different data types

print(values[0])   #1

print(values[3])   #4

print(values[-1])  #5  - If you want last value give -1

print(values[1:3]) #[2, 'mridhu'] - sub list last value it will not include like java sub String

values.insert(3, "sree")  #[1, 2, 'mridhu', 'sree', 4, 5] - insert sree in 3rd index
print(values)

values.append("SMS") #[1, 2, 'mridhu', 'sree', 4, 5, 'SMS']  - It will add at the end
print(values)

values[2] ="MRIDHU" #[1, 2, 'MRIDHU', 'sree', 4, 5, 'SMS']  - updating new value
print(values)

del values[0]       #[2, 'MRIDHU', 'sree', 4, 5, 'SMS']   - deleting value based on index
print(values)


# f stands for formatted string
fruit = "apple"
print("Frist fruit: {fruit}")
#Python treats {fruit} as plain text

fruit = "apple"
print(f"Frist fruit: {fruit}")


