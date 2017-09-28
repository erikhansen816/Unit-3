#Erik Hansen
#9/27/2017
#unitConverter.py - converts units


print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')

while True:
    opt = (input('Choose a number or type quit: '))
    if opt == '1':
        km = float(input('Enter number of Kilometers: '))
        print(km, 'kilometers is',km*.621,'miles')
    elif opt == '2':
        kg = float(input('Enter a number of Kilograms: '))
        print(kg, 'kilograms is',kg*2.204,'pounds')
    elif opt == '3':
        l = float(input('Enter a number of Liters: '))
        print(l, 'liters is',l*.264,'gallons')
    elif opt == 'quit':
        break
    else:
        c = float(input('Enter degrees in Celcius: '))
        print(c, 'degrees Celsius is',c*1.8+32,'degrees Fahrenheit')
    
