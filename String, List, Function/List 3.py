#Count Strings with Same Start and End
l = ['apple', 'banana', 'level', 'radar', 'hello', 'world', 'noon', 'python']
count = 0
for i in l:
    if i[0] == i[-1]:
        count += 1
print("Count of strings with same start and end character:", count)