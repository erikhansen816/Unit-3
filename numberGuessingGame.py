#Erik Hansen
#9/28/2017
#numberGuessingGame - guessing a number

from random import randint
tries = 0
num = randint(1,100)
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess>num:
        print('Your guess is too high')
    elif guess<num:
        print('Your guess is too low')
    else:
        tries = tries + 1
    
        break
    tries = tries + 1
print('You got it in', tries, 'tries')
