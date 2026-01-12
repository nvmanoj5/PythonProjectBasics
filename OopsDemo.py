#classes are user defined blueprint or prototype
#It contains class variables, instance variables, constructor etc


class calcualtor:
    num = 100  #class variables

    #default constructor
    def __init__(self):
        print("Constructor automatically called when object is created")

    def getData(self):
        print("I am now executing as method in class")

obj = calcualtor() #syntax to create object
obj.getData() #calling method
print(obj.num) #calling variable