print("\nOperations : \n")
print(" 1. + \n 2. - \n 3. * \n 4. / \n")

while True:
    a = int(input("Enter 1st number : "))
    op = input("Operator : ")
    b = int(input("Enter 2nd number : "))

    if op == "+":
        print(f"{a} + {b} = {a+b}")
    elif op == "-":
        print(f"{a} - {b} = {a-b}")
    elif op == "*":
        print(f"{a} x {b} = {a*b}")
    elif op == "/":
        print(f"{a} / {b} = {a/b}")
    else:
        print("<< INVALID OPERATOR INPUT >>")

    choice = input("Do you want to continue? (y/n) : ").strip().lower()
    if choice != "y":
        print("Exiting calculator.")
        break
