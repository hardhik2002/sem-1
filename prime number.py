num=int(input("Enter a number to check weather it is prime or not:"))
for i in range(2,num):
    if num%i==0:
        print("Not prime.")
        break
else:
    print("Prime.")