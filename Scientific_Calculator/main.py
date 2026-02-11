from basic_operations import add, subtract, multiply, divide
from advanced_operations import square_root, power, sin_deg

def main():
    print("Scientific Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sin (Degrees)")

    choice = input("Choose operation: ")

    if choice in ['1', '2', '3', '4', '6']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    elif choice == '5':
        x = float(input("Enter number: "))
        print("Result:", square_root(x))
    elif choice == '6':
        print("Result:", power(a, b))
    elif choice == '7':
        x = float(input("Enter angle in degrees: "))
        print("Result:", sin_deg(x))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
