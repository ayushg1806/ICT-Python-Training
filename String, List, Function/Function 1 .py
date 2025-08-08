#Factorial of a Number
def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n
print(factorial(9))