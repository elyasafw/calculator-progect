import functions as f

def menu():
    print("1. add\n\
2. subtraction\n\
3. multiplication\n\
4. division\n\
5. holding\n\
6. root\n\
7. absolute value\n\
8. triangular area\n\
9. square/rectangle area\n\
10. circle area")
    while True:
        user_operation = input("Please select the desired calculation operation (1-10):  ")
        if not user_operation.isdigit() or 0 >= int(user_operation) or 10 < int(user_operation):
            print("Please select again..")
        else:
            break

    return user_operation


def user_nums(user_operation):
    while True:
            if user_operation == "7" or user_operation == "10":
                user_number1 = input("Enter a number to calculate:  ")
                user_number2 = 1
                try:
                    user_number1 = float(user_number1)
                    break
                except ValueError:
                    print("Please enter numbers only!")
            elif user_operation == "6":
                user_number1 = input("Enter a base number for calculation:  ")
                user_number2 = input("Enter a secondary number for calculation:  ")
                try:
                    user_number1 = float(user_number1)
                    if user_number2 == "":
                        user_number2 = 2
                        break
                    else:
                        user_number2 = float(user_number2)
                        break
                except ValueError:
                    print("Please enter numbers only!")
            else:
                user_number1 = input("Enter a base number for calculation:  ")
                user_number2 = input("Enter a secondary number for calculation:  ")
                try:
                    user_number1 = float(user_number1)
                    user_number2 = float(user_number2)
                    break
                except ValueError:
                    print("Please enter numbers only!")

    operations_list = [f.add(user_number1, user_number2),
                       f.func_sub(user_number1, user_number2),
                       f.multiply(user_number1, user_number2),
                       f.divide(user_number1, user_number2),
                       f.holding(user_number1, user_number2),
                       f.root(user_number1, user_number2),
                       f.absolute_value(user_number1),
                       f.triangle_area(user_number1, user_number2),
                       f.square_area(user_number1, user_number2),
                       f.calculate_circle(user_number1)]
    

    print(operations_list[int(user_operation) - 1])