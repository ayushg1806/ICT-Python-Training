#nteger Filter Lambda
var1 = lambda x: x % 2 == 0
var2 = lambda x: x % 2 != 0
def filter_numbers(lst, condition):
    return list(filter(condition, lst))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], var1))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], var2))
