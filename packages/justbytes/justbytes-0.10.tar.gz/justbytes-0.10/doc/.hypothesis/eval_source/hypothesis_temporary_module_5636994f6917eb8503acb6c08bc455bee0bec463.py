from hypothesis.utils.conventions import not_set

def accept(f):
    def testNonRepeatingDecimal(self, divisor=not_set, multiplier=not_set):
        return f(self, divisor, multiplier)
    return testNonRepeatingDecimal
