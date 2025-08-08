#Validate Integer Input and Raise ValueError
try:
    num = int(input('Enter an integer: '))
    print(f'You entered: {num}')
except:
    print('Invalid input')
