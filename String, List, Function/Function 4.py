#Print Even Numbers from a Given List
def even_numbers(lst):
    for i in lst:
        if i % 2 == 0:
            print(i, end=' ')
    return ''

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))