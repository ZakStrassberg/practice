class Underscore(object):
    def map(self, list, iteratee):
        return [iteratee(each) for each in list]

    def reduce(self, list, iteratee, *memo):
        pass

    def find(self):
        pass

    def filter(self):
        pass

    def reject(self):
        pass


# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore()  # yes we are setting our instance to a variable that is an underscore

print _.map([1, 2, 3], lambda x: x ** 2)

evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print evens
