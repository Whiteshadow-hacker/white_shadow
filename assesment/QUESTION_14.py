def sum_of_primes(num):
    isPrime = 1
    for i in range (2,int(num/2),1):
        if(num % i == 0):
            isPrime = 0
            break
    return isPrime

num = int(input("Enter a number : "))
flag = 0
i = 2
for i in range (2,int(num/2),1):
    if(sum_of_primes(i) == 1):
        if(sum_of_primes(num-i) == 1):
            print(num,"can be expressed as the sum of",i,"and",num-i)
            flag = 1
if (flag == 0):
    print(n,"cannot be expressed as the sum of two prime numbers")
