#Square & Cube Lambda
square = lambda x: x ** 2
cube = lambda x: x ** 3
def opeations(lst, operation):
    return list(map(operation, lst))
print(opeations([1, 2, 3, 4, 5], square))
print(opeations([1, 2, 3, 4, 5], cube))