class Calculator:
    def __init__(self):
        self.operations = {
            "1": ("Addition", self.add),
            "2": ("Subtraction", self.subtract),
            "3": ("Multiplication", self.multiply),
            "4": ("Division", self.divide),
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        
        if b != 0:
            return a / b
        return "Error: Division by zero is not executable."

    def display_menu(self):
        
        print("Welcome to Ray's Calculator!")
        print("Choose an operation:")
        for key, (name, _) in self.operations.items():#key-value pair maps a menu choice to an operation.

            print(f"{key}. {name}")

    def get_operation_choice(self):
        
        while True:
            choice = input("Enter the number corresponding to the operation (1-4) or 'q' to quit: ")
            if choice in self.operations or choice == 'q':
                return choice
            print("Invalid choice. Please try again.")

    def get_numbers(self):
        
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                return num1, num2
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_operation_choice()

            if choice == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            operation_name, operation_function = self.operations[choice]
            print(f"You selected: {operation_name}")

            num1, num2 = self.get_numbers()
            result = operation_function(num1, num2)

            print(f"The result is: {result}")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
