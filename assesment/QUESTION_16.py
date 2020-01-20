from collections import OrderedDict
str=input("enter the string:")
result = "".join(OrderedDict.fromkeys(str))
print()
print(result)


