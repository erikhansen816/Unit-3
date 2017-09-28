#Erik Hansen
#9/28/2017
#breakDemo.py - how to exit a loop early

#copy cat
while True:
    text = input('Type something: ')
    print(text)
    if text == 'something':
        break
    
print('You win')
