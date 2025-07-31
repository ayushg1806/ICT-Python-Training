import time
def measure_execution_time(func):
    def wrapper(*a, **ka):
        start = time.time()
        result = func(*a, **ka)
        end = time.time()
        execution_time = end - start
        print(f'Function {func.__name__} took {execution_time:.4f} seconds to execute')
        return result
    return wrapper

@measure_execution_time
def calculate_multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

result = calculate_multiply([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Result:', result)