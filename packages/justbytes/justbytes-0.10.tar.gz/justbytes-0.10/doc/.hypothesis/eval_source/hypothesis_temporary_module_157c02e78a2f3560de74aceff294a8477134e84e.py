from hypothesis.utils.conventions import not_set

def accept(f):
    def testMoreComplexRepeatingDecimal(self, divisor=not_set, multiplier=not_set):
        return f(self, divisor, multiplier)
    return testMoreComplexRepeatingDecimal
