# This is a function that accepts 2 numbers and returns their subtraction.
def func_sub(num1, num2):
    try:
        return num1-num2
    except ValueError,TypeError:
        return "Please select a number"
    
