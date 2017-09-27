#Erik Hansen
#9/27/2017
#fives.py - finds multiples of five until number

num = int(input('Enter a number: '))
for i in range(1,num+1):
    if i%5 == 0:
        print(i)
