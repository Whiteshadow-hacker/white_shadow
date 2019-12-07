def series(n):
    a=list()
    for i in range(1,n+1):
        a.append(i)
    for i in range(n-1,0,-1):
        a.append(i)
    for i in a:
        print(i,end=" ")
n=int(input("enter the number:"))
x=(n+(n-2))
for i in range(1,n+1):
    print(" "*x,end="")
    series(i)
    print()
    x-=2
y=2
for i in range(n-1,0,-1):
    print(" "*y,end="")
    series(i)
    print()
    y+=2
