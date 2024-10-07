class InfiniteCounter:
    def __init__(self, start):
      self.current = start

    def __next__(self):
      num = self.current
      self.current += 1
      return num
    
    def __iter__(self):
      return self
      
# infinitenumbers = InfiniteCounter(5)
# for el in infinitenumbers:
#    print(infinitenumbers.current)

class PrimeNumberIterator:
    
    @staticmethod
    def _is_prime(number) -> bool:
      if number <= 1:
         return False
      
      if number == 2:
         return True
      
      if number % 2 == 0:
         return False

      for i in range(3, int(number**0.5) + 1):
         if number % i == 0:
            return False

    def __init__(self, start):
      self.current = start

    def __next__(self):
      while True:
          if PrimeNumberIterator._is_prime(self.current):
              temp = self.current
              self.current += 1
              return temp
          self.current += 1


    def __iter__(self):
      return self
   
class DigitSumIterator:
    @staticmethod
    def _sum_of_digits(number: int):
        sum = 0      
        while number != 0:
          sum += number % 10
          number = number // 10
        return sum
    
    # 2nd version calculating sum of number's digits
    # def _sum_of_digits(self,  number):
    #     digit_sum = 0
    #     for digit in str(number):
    #         digit_sum += int(digit)
    #     return digit_sum

    def __init__(self, start):
      self.current = start
    
    def __next__(self):
      temp = self.current
      sum = DigitSumIterator._sum_of_digits(temp)
      self.current += 1
      return sum
    
    def __iter__(self):
      return self

number_digit_sum_iterator = DigitSumIterator(12)  
for _ in range(10):
    print(next(number_digit_sum_iterator))
