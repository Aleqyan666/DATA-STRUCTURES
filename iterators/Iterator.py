class InfiniteCounter:
    def __init__(self, start):
      self.current = start

    def __next__(self):
      current_value = self.current
      self.current += 1
      return current_value
    
    def __iter__(self):
       return self


def infinite_counter(start):
    current = start
    while True:
        yield current
        current += 1

# Start counter from 10
counter_gen = infinite_counter(10)

for _ in range(10):
    print(next(counter_gen))

if __name__ == "__main__":
    counter = InfiniteCounter(5)  # Start from 5
    for _ in range(10):  
        print(next(counter))


