import random
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
number = random.randint(num1, num2)
guesses = 10
guess_try = 0
err = 0

while True:
    try:
        guess = int(input(f'Guess a number between {num1} and {num2}, you have {guesses} guesses \n'))

        while True:
            if guesses == 0:
                print('you lost')
                break
            elif guess > number:
                guesses -= 1
                guess_try += 1
                print(f'its LESS, guess again you have {guesses} guesses left')
                guess = int(input())
            elif guess < number:
                guesses -= 1
                guess_try += 1
                print(f'its MORE, guess again you have {guesses} guesses left')
                guess = int(input())
            else:
                guess_try += 1
                print(f'thats it, congratulations you got it in {guess_try} tries !')
                break

    except:
        print('invalid input')
        continue
    if guess == number:
        break
