first = int(input("Enter the 1st number: "))
second = int(input("Enter the 2nd number: "))
op = input("Enter the operation: ")
if op == '+':
    print(first + second)
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    if second != 0:
        print(first / second)
    else :
        print("Error! Division by zero is not allowed.")
else :
    print("Invalid operation. Please enter either +, -, * or /")
