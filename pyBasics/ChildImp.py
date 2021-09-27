from pyBasics.OopsDemo import Calc

class ChildImpl(Calc):
    num2 = 200

    def __init__(self):
        Calc.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
