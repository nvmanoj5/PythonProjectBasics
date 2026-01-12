#self keyword is mandatory for calling variables names into methods
#constructor name should be _init__
#instance and class variable have whole different purpose
#new keyword is not required when you create object

class calc:
    num = 100

    def __init__(self, a, b):  # self is object...obj will be passed as a first argument and we call it as self
        self.firstNumber = a
        self.secondNumber = b


    def summation(self):
        return self.firstNumber + self.secondNumber + calc.num  


obj = calc(4, 5) #syntax to create object
print(obj.summation())