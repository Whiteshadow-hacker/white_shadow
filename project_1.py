boy=[]
girl=[]
common=[]
nameb=str(input("enter the name of boy without spaces:"))
nameg=str(input("enter the name of girl without spaces:"))
for i in nameb:
    boy.append(i)
for i in nameg:
    girl.append(i)
def intersection(a,b): 
    return list(set(a) & set(b)) 
common=intersection(boy,girl)
n=((len(boy)+len(girl))-(2*len(common)))
print()
lst=[1,2,3,4,5,6]
z=(n-1)
if z==6:
    z-=len(lst)
elif z>len(lst):
    while z>len(lst):
        z-=len(lst)
    if z==len(lst):
        z-=len(lst)
lst.pop(z)
x=z+(n-1)
while len(lst)>1:
    if x<len(lst):
        lst.pop(x)
        x+=(n-1)
    else:
        while x>=len(lst):
            x-=len(lst)
        lst.pop(x)
        x+=(n-1)
print('*'*50)
print('*'*50)
print()
if lst==[1]:
    print(nameb,nameg," are friends")
elif lst==[2]:
    print(nameb," loves ",nameg)
elif lst==[3]:
    print(nameb," has an affection on ",nameg)
elif lst==[4]:
    print(nameb," weds ",nameg)
elif lst==[5]:
    print(nameb," and ",nameg," are enemies")
elif lst==[6]:
    print(nameg," is a sister of ",nameb)
print()
print('*'*50)
print('*'*50)

        
        


    
