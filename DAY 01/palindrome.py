s = input("Enter the word : ")
temp = s.lower()  
org = s.lower()

temp = temp[::-1]

if(temp == org):
    print(f"{s} is Palindrome.")
else:
    print(f"{s} is not Palindrome.")
