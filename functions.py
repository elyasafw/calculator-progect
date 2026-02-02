#function add num 1 +num 2
def add(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
         return "You can only perform arithmetic operations on numbers!"

      
# This is a function that accepts 2 numbers and returns their subtraction.
def func_sub(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 - num2
    else:
        return "You can only perform arithmetic operations on numbers!"
    
    
# A function that performs a multiplication operation between 2 numbers
def multiply(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 * num2
    else:
        return "You can only perform arithmetic operations on numbers!"
    
# Root calculation function with a dipole value of 0.5
def root(num1, num2 = 2):
    try:
        return num1**(1/num2)
    except ValueError,TypeError:
        return "Please select a number"

#function that divider num 1 / num 2
def divide(num1, num2):
    if num2 <= 0 or num1 <= 0:
        return "division by zero!"
    elif type(num1) != int and type(num2) != int:
        return "Please enter numbers only"
    else:
        return num1/num2

    
# Function that calculates the area of ​​a square and a rectangle
def square_area(Length, width):
    if not (isinstance(Length, (int, float)) and isinstance(width, (int, float))):
        return "You can only perform area calculations on numbers!"
    if Length <= 0 or width <= 0:
        return "There is no area size with value 0 or less.."
    return Length * width

    
# A function that accepts a radius array and returns the circumference of a circle
def calculate_circle(radius):
    if not isinstance(radius, (int, float)):
        return "Only numbers can be calculated."
    if radius <= 0:
        return "Cannot calculate 0 or negative radius.."
    pi_approx = 3.14159
    return pi_approx * (radius ** 2)

  
#that function calculate num1 ** num2
def holding(num1, num2):
    try:
        return num1 ** num2
    except (ValueError,TypeError,ZeroDivisionError):
        return "Invalid input for power calculation"
      
      
#htat function return absolute the num1
def absolute_value(num1):
    try:
        return abs(num1)
    except TypeError:
        return "Please enter numbers only"

      
def triangle_area(base, height):
    try:
        return base * height
    except ValueError,TypeError:
        return "Please select a number"