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
    

# Function that calculates the area of ​​a square and a rectangle
def square_area(Length, width):
    if type(Length) == int and type(width) == int:
        return Length * width
    elif Length <= 0 or width <= 0:
        return "There is no area size with value 0.."
    else:
        return "You can only perform area calculations on numbers!"