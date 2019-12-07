print("1.usd -> inr")
print("2.euro -> inr")
print("3.pound -> inr")
print("4.sd -> inr")
print("5.ringgir -> inr")
print('$'*20,'currency converter','$'*20)
print()
k=int(input("enter your choice:"))
if k == 1:
    usd=float(input("enter the amount in usd:"))
    print(usd*70.875)
elif k == 2:
    euro=float(input("enter the amount in euros:"))
    print(euro*77.9385)
elif k == 3:
    pound=float(input("enter the amount in pounds:"))
    print(pound*88.18)
elif k == 4:
    sd=float(input("enter the amount in sd:"))
    print(sd*51.49)
elif k == 5:
    ring=float(input("enter the amount in ringgits:"))
    print(ring*16.95)
print()
print('$'*20,'THANKYOU','$'*20)

    