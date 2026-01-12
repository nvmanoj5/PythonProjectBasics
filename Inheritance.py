from Constructor import calc


class child(calc):
    num2 = 200

    def __init__(self):
        calc.__init__(self, 5, 7)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = child()
print(obj.getCompleteData())