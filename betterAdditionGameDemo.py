#Erik Hansen
#10/4/2017
#betterAdditionGameDemo.py - ask addition problems until user gets 5

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is ' + str(num1) + '+' + str(num2) + '? '
    answer = int(input(question))
    if num1 + num2 == answer:
        print('Correct')
        numCorrect += 1
    else:
        print('WRONG YOU DUMB IMBECILE! The real answer was', num1+num2)
print("Congratulations... you can do simple math computation as a high schooler. Here's your participation award.")
