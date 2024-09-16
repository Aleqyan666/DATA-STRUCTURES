class DigitSumIterator:

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        """
        Returns the sum of digits of the current number and advances the iterator.
        """
        if self.current < 0:
            raise StopIteration

        digit_sum = self._sum_of_digits(self.current)
        self.current += 1
        return digit_sum
    
    def _sum_of_digits(self,  number):
        digit_sum = 0
        for digit in str(number):
            digit_sum += int(digit)
        return digit_sum

iterator = DigitSumIterator(10)
for _ in range(5):
    print(next(iterator))
    