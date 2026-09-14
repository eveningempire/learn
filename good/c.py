from good.b import number

class supernumber(number):
    def __init__(self, value, cmj):
        super().__init__(value)
        self.cmj=cmj

    def is_positive(self):
        return self.value > 0

    def is_negative(self):
        return self.value < 0