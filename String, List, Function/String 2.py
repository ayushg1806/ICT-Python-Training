#Count character frequency in a string
st = 'hello world'
count = {}
for i in st:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print("Character frequency:", count)
    