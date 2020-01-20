str=input("enter the string:")
bit=list()
for i in str :
    if i != '0' or i != '1':
        bit.append(i)
if not bit:
    print("the string contains only 0 or 1")
else:
    print("the string does not contain only 0 or 1")

