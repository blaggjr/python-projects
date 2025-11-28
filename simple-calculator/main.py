# This function adds two numbers
def add(x, y):
    return x + y


# This subtracts adds two numbers
def subtract(x, y):
    return x - y


# This multiplies adds two numbers
def multiply(x, y):
    return x * y


# This divides adds two numbers
def divide(x, y):
    return x / y


# Main function
def main():
    # Display menu
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Get input from user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number:"))
            except:
                print("Invalid input. Please enter a number.")
                continue

            if choice == "1":
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == "4":
                try:
                    print(num1, "/", num2, "=", divide(num1, num2))
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # Check if the user wants another calculation
            # break out of loop if the answer is no
            next_calculation = input("Let's do another calculation? (yes/no): ")
            while next_calculation.lower() not in ("yes", "no", "y", "n"):
                print("Invalid choice.")
                next_calculation = input("Let's do another calculation? (yes/no): ")

            if next_calculation.lower() in ("no", "n"):
                break
            elif next_calculation.lower() in ("yes", "y"):
                continue
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
