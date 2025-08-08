#List Permutations Generator
from itertools import permutations
def list_permutations(lst):
    for perm in permutations(lst):
        yield perm
lst = [1, 2, 3]
for perm in list_permutations(lst):
    print(perm)