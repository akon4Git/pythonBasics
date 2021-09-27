#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object


class Calc:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calc.num


obj = Calc(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calc(4, 5)
obj1.getData()
print(obj1.Summation())



