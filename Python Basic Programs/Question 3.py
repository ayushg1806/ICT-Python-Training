#Number Guessing Game
import random
userNumber = int(input("Enter a number between 1 and 9: "))
randomNumber = random.randint(1, 9)
while True:
    if userNumber == randomNumber:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("Wrong guess. Try again!")
        userNumber = int(input("Enter a number between 1 and 9: "))
        randomNumber = random.randint(1, 9)
