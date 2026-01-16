ItemsInCart =0

if ItemsInCart != 2: # raise Exception("Products cart count not matching")  #Commented it will fail
    print("Pass")

try:
    with open('store.txt','r') as reader:
        reader.read()

except:
    print("Failure is there - reached catch block")

try:
    with open('store.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources - finally block")