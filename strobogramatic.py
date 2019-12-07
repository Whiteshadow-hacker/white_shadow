a=input("enter the number:")
b=[]
c=[]
k=0
for i in a:
    b.append(i)
    c.append(i)
while k<len(b):
    if b[k]=='6':
        b[k]='9'
    elif b[k]=='9':
        b[k]='6'
    k+=1
b.reverse()
if b==c:
    print("it is a strobogramatic number")
else:
    print("it is not a strobogramatic number")

