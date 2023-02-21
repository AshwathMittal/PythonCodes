import random
import sys
a = random.randint(1, 10)

score = 0

while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
    except ValueError:
        print('Please enter a number')
    if guess == a:
        print("You guessed it!")
        score += 1
        print("Your score is:", score)
    elif guess == 0:
        print("Your score is:", score)
        sys.exit()
    elif guess < a:
        print("Too low!")
    elif guess > a:
        print("Too high!")
        
        
