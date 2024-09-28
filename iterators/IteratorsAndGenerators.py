def my_gen():
    yield 1
    yield 2
    yield 4
    yield 6


class PythonGeneratedClassGenerator:
    def __init__(self):
        self._cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur == 1:
            self._cur = 2
            return 1
        elif self._cur == 2:
            self._cur = 4
            return 2
        elif self._cur == 4:
            self._cur = 6
            return 4
        elif self._cur == 6:
            self._cur = -1
            return 6
        else:
            raise StopIteration





# Even if we call the method generator it will not become one unless it has yield call in it
def generator():
    x = 7


# check the return value of a function w/o return statement
print(generator()) # Output: None
# check the return value of a function w/o return statement but with yield call
print(my_gen()) # Output: <generator object my_gen at 0x102bc8700>
# So generator methods are special functions that are generating data and their output is a generator object.
# Generator object is an iterator, as it implements iterator design pattern (protocol) - has iter and next methods
e = my_gen()


# class Generator:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
#
# gg = Generator()
# print(gg)
#
# for i in e:
#     pass
#
# # it = gg.__iter__()
# # while True:
# #     try:
# #         next(it)
# #     except StopIteration:
# #         break
# for i in gg:
#     pass


# The generator object will provide an output through next(gen-object) call as many times, as many yield calls it has
print(next(e))
print(next(e))
print(next(e))
print(next(e))
# print(next(e)) # This call will generate StopIteration exception

gg = PythonGeneratedClassGenerator()
print(next(gg))
print(next(gg))
print(next(gg))
print(next(gg))
# print(next(gg)) # This call will generate StopIteration exception



def even_gen():
    num = 0
    while True:
        yield num
        num += 2


# If the generator has infinite yield calls, then it will generate infinite number of values
e1 = even_gen()

# Code below will generate infinite loop, as the generator object is iterable, and we are iterating on infinite sequence
# for i in e1:
#     print(i)

# If we have an infinite generator, we should use it in finite loops. See an example below
for i in range(10):
    print("add 5 to even - ", next(e1) + 5)

e1 = even_gen()
for i in range(10):
    print("add 3 to even - ", next(e1) + 3)


# We can also implement a generator which receives argument(s) and uses them to stop the generation at some point
def even_gen_with_upper_limit(lim):
    num = 0
    while num <= lim:
        yield num
        num += 2


# Here we can use the generator in foreach loop as an iterable object, as it is generating a finite sequence
e2 = even_gen_with_upper_limit(20)
for i in e2:
    print(i)


# This generator will generate the fibonacci numbers.
def fib_gen():
    n_1 = 0
    n = 1
    while True:
        yield n_1
        t = n + n_1
        n_1 = n
        n = t


fib = fib_gen()
print("Print first 10 fib numbers")
for i in range(10):
    print(next(fib))


# Now let's implement an iterator, which will iterate over even numbers similar to even number generators above
class EvenNumIterator:
    def __init__(self, max=float('inf')):
        self._max = max
        self._cur = 0

    # Overwriting the __iter__ method to make the iterator also iterable, which will allow us to use it in for loop
    def __iter__(self):
        return self

    def __next__(self):
        if self._cur >= self._max:
            raise StopIteration
        temp = self._cur
        self._cur += 2
        return temp


it = EvenNumIterator(10)
for i in it:
    print(i)

# Putting below the generator usage, to note that both behave the same way
e2 = even_gen_with_upper_limit(10)
for i in e2:
    print(i)


# Python has also a notion of generator expressions, which is even a shorter way of creating generator objects
x = (i * 5 for i in range(5))
evens = x = (i for i in range(0, float('inf'), 2))
print(x) # Output: <generator object <genexpr> at 0x102afc040>
for i in x:
    print(i)


class SquareIterator:
    def __init__(self, max=float('inf')):
        self.cur = 0
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
      if self.cur > self.max:
          raise StopIteration
      result = self.cur ** 2
      self.cur += 1
      return result
    
# square_iter = SquareIterator(max=10)
# for el in square_iter:
#     print(el)

class SquareGenerator:
    def __init__(self, max=float('inf')):
        self.cur = 1
        self.max = max

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur > self.max:
            raise StopIteration
        result =  self.cur ** 2
        self.cur += 1
        return result
    
class FactorialIterator:
    def __init__(self, max):
      self.cur = 1
      self.max = max
      self.product = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur > self.max:
            raise StopIteration
        self.product *=  self.cur
        self.cur += 1
        return self.product

def factorial_generator(max: int):
    start, product = 1, 1
    while start <= max:
        product *= start
        yield product
        start += 1
        
# for element in factorial_generator(5):
#     print(element)

class GeometricProgressionIterator:
    def __init__(self, start, ratio, count):
        self.start = start
        self.ratio = ratio
        self.count = count
        self.cur = 0 

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur >= self.count:
            raise StopIteration
        
        result = self.start * (self.ratio ** self.cur)
        self.cur += 1
        return result
    
import random


def geometric_progression_generator(start, ratio, count):
    cur = 0
    while cur < count:
        result = start * (ratio ** cur)
        yield result
        cur += 1

for element in geometric_progression_generator(5, 2.5, 6):
    print(element)


def random_number_generator(low, high, count):
    for _ in range(count):
        yield random.randint(low, high)

for number in random_number_generator(1, 100, 5):
    print(number)