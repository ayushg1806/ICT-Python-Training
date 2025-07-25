#Count Even and Odd Numbers in a series
numbers = (1,2,3,4,5,6,7,8,9)
countEven, countOdd = 0, 0
for i in numbers:
    if i % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print("Count of Even Numbers:", countEven)
print("Count of Odd Numbers:", countOdd)