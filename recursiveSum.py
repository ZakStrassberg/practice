class MathDojo(object):
    def __init__(self):
        self.result = 0

    def recursiveSum(self, arg, summed=0):
        if isinstance(arg, (list, tuple)):
            for items in arg:
                summed += self.recursiveSum(items)
        else:
            summed += arg
        return summed

    def add(self, ints, *additionalInts):
        self.result += self.recursiveSum(ints)
        self.result += self.recursiveSum(*additionalInts)
        return self

    def subtract(self, ints, *additionalInts):
        self.result -= self.recursiveSum(ints)
        self.result -= self.recursiveSum(*additionalInts)
        return self

print MathDojo().add(2).add(2, 5).subtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
