#Random Number Generator
import random
def random_numbers(n):
    for _ in range(n):
        yield random.randint(1, 100)
        
for num in random_numbers(10):
    print(num)