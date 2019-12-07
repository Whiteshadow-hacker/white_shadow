n=int(input("enter the number:"))
i=2
div=list()
if n==1:
    print("it is neither prime nor composite")
else:
    while i<n:
        if n%i==0:
            div.append(i)
        i+=1
    if not div:
        print("it is a prime number")
    else:
        print("it is a composite number")
    
