class addition:

    def __init__ (self,f,s):  ##This will execute whenever addition class will be called
        self.first=f
        self.second=s

    def calculate(self):
        print(self.first + self.second)

obj=addition(6,7) #

obj.calculate()
obj.calculate()