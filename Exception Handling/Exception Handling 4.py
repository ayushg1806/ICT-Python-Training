#Validate Numerical Inputs and Raise TypeError
try:
    num = float(input('Enter a number:'))
    print(num)
except ValueError:
    print('Invalid input. Please enter a valid number.')