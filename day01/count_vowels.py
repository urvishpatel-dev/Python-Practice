text = input("Enter the string : ")

text = text.lower().replace(" ","")

count = 0
for i in text:
    if(i in ("a","e","i","o","u")):
        count +=1

print(f"{count} vowels in string.")