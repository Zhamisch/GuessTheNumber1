import random

__import__("random")
def guess(x):
    number1=random.randint(1,x)
    guess=0
    while guess != number1:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess > number1:
            print("Too high.Try again")
        elif guess<number1:
            print("Too low.Try again")
    print(f'Well done!.{number1} is correct')
guess(12)







