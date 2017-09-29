#Erik Hansen
#9/29/2017
#divisors.py

num = int(input('Enter a number: '))
total = 0
for i in range(1,num):
    if num%i==0:
        total = total + i
if total == num:
    print('Perfect')
else:
    print('Not perfect')

