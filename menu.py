import functions as f

def display_options():
    print("\n-- Calculator Menu --")
    options = [
        "Add", "Subtraction", "Multiplication", "Division", "Holding",
        "Root", "Absolute Value", "Triangular Area", "Square/Rectangle Area", "Circle Area"
    ]
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

def get_user_choice():
    while True:
        choice = input("Select operation (1-10):  ")
        if choice.isdigit() and 1 <= int(choice) <= 10:
            return choice
        print("Invalid choice.. Please select 1-10!")

def process_calculation(op):
    functions_map = {
        "1": f.add, "2": f.func_sub, "3": f.multiply, "4": f.divide,
        "5": f.holding, "6": f.root, "7": f.absolute_value,
        "8": f.triangle_area, "9": f.square_area, "10": f.calculate_circle
    }

    try:
        if op in ["7", "10"]:
            num1_input = float(input("Enter number:  "))
            return functions_map[op](num1_input)
            
        elif op == "6":
            num1_input = float(input("Enter base number:  "))
            num2_input = input("Enter root degree (default 2):  ")
            if num2_input != "":
                num2 = float(num2_input) 
            else:
                num2 = 2
            return f.root(num1_input, num2)
            
        else:
            num1_input = float(input("Enter first number:  "))
            num2_input = float(input("Enter second number:  "))
            return functions_map[op](num1_input, num2_input)

    except ValueError:
        return "Error: Please enter valid numbers only!"