#function add num 1 +num 2
def add(num1, num2):
        return num1 + num2

      
# This is a function that accepts 2 numbers and returns their subtraction.
def func_sub(num1, num2):
        return num1 - num2
    
    
# A function that performs a multiplication operation between 2 numbers
def multiply(num1, num2):
        return num1 * num2

    
# Root calculation function with a dipole value of 0.5
def root(num1, num2):
    try:
        return num1**(1/num2)
    except ZeroDivisionError:
        return "Cannot be divided by 0 or less.."

#function that divider num 1 / num 2
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
         return "Cannot be divided by 0 or less.."

    
# Function that calculates the area of ​​a square and a rectangle
def square_area(Length, width):
    if Length <= 0 or width <= 0:
        return "There is no area size with value 0 or less.."
    return Length * width

    
# A function that accepts a radius array and returns the circumference of a circle
def calculate_circle(radius):
    if radius <= 0:
        return "Cannot calculate 0 or negative radius.."
    pi_approx = 3.14159
    return pi_approx * (radius ** 2)

  
#that function calculate num1 ** num2
def holding(num1, num2):
    return num1 ** num2
      
      
#htat function return absolute the num1
def absolute_value(num1):
    return abs(num1)

      
def triangle_area(base, height):
    return base * height