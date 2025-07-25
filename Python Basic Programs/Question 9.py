#Fibonacci Series
a, b = 0, 1
i = 0
while i < 51:
    print(b, end=" ")
    a, b = b, a + b
    i += 1
    