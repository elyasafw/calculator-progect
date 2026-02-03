import menu

def start_calculate():
    while True:
        menu.display_options()
        choice = menu.get_user_choice()
        result = menu.process_calculation(choice)
        
        print(f"\n>>> Result: {result}")
        
        if input("\nDo another calculation? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    start_calculate()