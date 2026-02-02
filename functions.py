#function add num 1 +num 2
def add(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
         return "Please enter numbers only"

      
# This is a function that accepts 2 numbers and returns their subtraction.
def func_sub(num1, num2):
    try:
        return num1-num2
    except ValueError,TypeError:
        return "Please select a number"
    
    
# A function that performs a multiplication operation between 2 numbers
def multiply(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 * num2
    else:
        return "You can only perform arithmetic operations on numbers!"