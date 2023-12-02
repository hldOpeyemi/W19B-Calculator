def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multipilication(x, y):
    return x * y
def division(x, y):
    return x / y

print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

choice = input("Enter choice (1 - 2 - 3 - 4): ")

if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
    except ValueError:
        print("Invalid Choice. Please enter a number")
    

    if choice == '1':
        print(num1, "+", num2, "=", addition(num1, num2))
    
    elif choice == '2':
         print(num1, "-", num2, "=", subtraction(num1, num2))

    elif choice == '3':
         print(num1, "*", num2, "=", multipilication(num1, num2))

    elif choice == '4':
         print(num1, "/", num2, "=", division(num1, num2))
    
    