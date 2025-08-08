#Cubes Generator
def cubes(n):
    for i in range(1, n+1):
        yield i ** 3
        
num = int(input("Enter a number: "))
for i in cubes(num):
    print(i)