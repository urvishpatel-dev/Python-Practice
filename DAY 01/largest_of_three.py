a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

print(f"\n1st num = {a} \n2nd num = {b} \n3rd num = {c}\n")

if(a>b):
    if(a>c):
        print(f"{a} is the largest of three numbers.")
    else:
        print(f"{c} is the largest of three numbers.")
elif(a<b):
    if(b>c):
        print(f"{b} is the largest of three numbers.")
    else:
        print(f"{c} is the largest of three numbers.")