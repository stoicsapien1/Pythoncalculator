def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    if b == 0:
        print("Error! Division by zero is not allowed.")
    else:
        answer = a / b
        print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")
    if choice.lower() == "a":
        print("Addition")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a, b)
    elif choice.lower() == "b":
        print("Subtraction")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a, b)
    elif choice.lower() == "c":
        print("Multiplication")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a, b)
    elif choice.lower() == "d":
        print("Division")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a, b)
    elif choice.lower() == "e":
        print("Program ended")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
