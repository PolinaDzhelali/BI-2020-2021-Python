print('hello. Welcome to unit converter for Russians;)')

convertation = int(input('What do you want to convert?: \n 1. Temperature\n 2. Mass\n 3. Length\n '))

     

# Fahrengeit -> Celsius

if convertation == 1:

    temperature = int(input(' 1. Fahrengeit to Celsius?\n '))

    if temperature == 1:

        value_temperature = float(input('Fahrengeit (enter the number):\n'))

    print(value_temperature, 'Fahrengeit = ', round(((5/9) * value_temperature - 32), 2), ' Celsius')
    
     

# Pounds -> Kilograms

if convertation == 2:

    massa = int(input(' 1. Pounds to Kilograms?\n'))

    if massa == 1:

        value_massa = float(input('Pounds (enter the number):\n'))

    print(value_massa, 'lb. =', round((value_massa * 0.453592), 2),'kg')

     

# Feet -> Meters

if convertation == 3:

    dlina = int(input(' 1. Feet to Meters?\n'))

    if dlina == 1:

        value_dlina = float(input('Feet (enter the number):\n'))

    print(value_dlina, 'ft. =', round((value_dlina / 3.28084), 2), 'm')
