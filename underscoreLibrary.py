class Underscore(object):
    def map(self, list, iteratee):
        return [iteratee(each) for each in list]

    def reduce(self, list, iteratee, memo=None):
        if memo is None:
            memo = list[0]
        returnValue = memo
        for each in list:
            returnValue += iteratee(0, each)
        return returnValue

    def find(self, list, predicate):
        for each in list:
            if predicate(each):
                return each
        return None

    def filter(self, list, predicate):
        filterList = []
        foundItem = False
        for each in list:
            if predicate(each):
                filterList.append(each)
                foundItem = True
        if foundItem:
            return filterList
        else:
            return None

    def reject(self, list, predicate):
        rejectList = []
        foundItem = False
        for each in list:
            if not predicate(each):
                rejectList.append(each)
                foundItem = True
        if foundItem:
            return rejectList
        else:
            return None


# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore()

print _.map([1, 2, 3], lambda x: x ** 2)
print _.reduce([1, 2, 3], lambda memo, num: memo + num, 0)
print _.find([1, 3, 3, 4, 5, 6], lambda num: num % 2 == 0)
print _.filter([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)
print _.reject([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0)

# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
# print evens
