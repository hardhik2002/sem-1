lst=[int(i) for i in input("Enter numbers:").split()]
prime=0
for i in lst:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime+=1
print("No of prime numbers:",prime)
