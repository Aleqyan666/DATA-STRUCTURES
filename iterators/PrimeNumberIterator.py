class PrimeNumberIterator:
    def __init__(self, start):
        """
        Initialize with a starting number and set it as the current number to check for primes.
        """
        self.current = start

    def __iter__(self):
        """
        This method makes the class itself an iterable. It returns the iterator object (self).
        """
        return self
      
    def __next__(self):
        """
        This method returns the next prime number starting from the current number.
        It increments the number until it finds a prime.
        """
        while True:
            if self.is_prime(self.current):
                prime_number = self.current
                self.current += 1
                return prime_number
            self.current += 1

    @staticmethod
    def is_prime(number):
        """
        Helper function to check if a number is prime.
        A prime number is only divisible by 1 and itself.
        """
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5 + 1)):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def prime_generator():
        """
        Generator function that yields an infinite sequence of prime numbers.
        """
        num = 2
        while True:
            if PrimeNumberIterator.is_prime(num):
                yield num
            num += 1

# Using the PrimeNumberIterator
if __name__ == "__main__":
    prime_iterator = PrimeNumberIterator(10)
    
    for _ in range(10):
        print(next(prime_iterator))

    prime_gen = PrimeNumberIterator.prime_generator()
    for _ in range(10):
        print(next(prime_gen))
