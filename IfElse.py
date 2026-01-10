greeting = "Good Morning"
print(greeting)

if(greeting=="Good Morning"):
    print("Condition matches")
    print("Condition matches:", greeting)
else:
    print("Condition do not matches")
    print("Condition do not matches:", greeting)

print("Out side if condition")

if greeting=="Good":  #without () parenthesis
    print("Condition matches")
else:
    print("Condition do not matches")

print("Out side if condition")

a=4

if a>2:
    print("Condition matches")
    print("Condition matches:", a)
else:
    print("Condition do not matches")
    print("Condition do not matches:", a)

# Checking both conditions

if greeting=="Good Morning" and a>2:
    print("Both Condition matches")
else:
    print("Both Condition do not matches")

if greeting=="Good" or a<2:
    print("One or more Condition matches")
else:
    print("Both Condition do not matches")


