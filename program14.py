# Q14. Menu-driven program using if-elif and loops

while True:
    print("\nMENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference =", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Product =", a * b)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")