#my first calculator
number1 = float(input('Enter first number:'))  #First number for calculation
operator = input('Choose operator (+ , - , *, / , ** , // , %)')
if operator != ('+', '-', '*', '/', '**' , '//' , '%'):
    result = "Your operator is not valid"
number2 = float(input('Enter second number:')) #Second number for calculation
if operator == '+': 
    result = number1 + number2  #addition
elif operator == '-': 
    result = number1 - number2  #subtraction
elif operator == '*': 
    result = number1 * number2  #multiplication
elif operator == '**': 
    result = number1 ** number2  #power
elif number2 != 0:  #check for division by zero
    if operator == '/': 
        result = number1 / number2  #division
    elif operator == '//':
        result = number1 // number2  #division without remainder
    elif operator == '%':
        result = number1 % number2  #remainder of division
elif number2 == 0: 
    result = "division by zero!" 
print(str("Result:"), result)




