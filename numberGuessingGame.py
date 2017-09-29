#Erik Hansen
#9/28/2017
#numberGuessingGame - guessing a number

from random import randint
tries = 0
num = randint(1,100)
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    tries = tries + 1
    if guess>num:
        print('Your guess is too high')
    elif guess<num:
        print('Your guess is too low')
    else:
        break
print('You got it in', tries, 'tries')
