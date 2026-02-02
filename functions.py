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
    

# Function that calculates the area of ​​a square and a rectangle
def square_area(Length, width):
    if not (isinstance(Length, (int, float)) and isinstance(width, (int, float))):
        return "You can only perform area calculations on numbers!"
    if Length <= 0 or width <= 0:
        return "There is no area size with value 0 or less.."
    return Length * width

    

# A function that accepts a radius array and returns the circumference of a circle
def square_circle(radius):
    if not isinstance(radius, (int, float)):
        return "Only numbers can be calculated."
    if radius <= 0:
        return "Cannot calculate 0 or negative radius.."
    pi_approx = 3.14159
    return pi_approx * (radius ** 2)