#Prime Generator (Range)
def prime(m, n):
    for num in range(m, n + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                yield num

for prime_num in prime(10, 50):
    print(prime_num)