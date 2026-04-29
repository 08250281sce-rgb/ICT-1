def sum(a, b):
    return a+b

def difference(a, b):
    return a-b

def product(a, b):
    return a*b

def quotient(a, b):
    if b == 0:
        return "Error"
    return a / b

while True:
    print("Calculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1 to 5): ")

    if choice == "5":
        print("Exiting the program...")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("The sum is:", sum(a,b))

    elif choice == "2":
        print("The difference is:", difference(a,b))

    elif choice == "3":
        print("The product is:", product(a,b))

    elif choice == "4":
        print("The quotient is:", quotient(a,b))

    else:
        print("please enter the correct choice")