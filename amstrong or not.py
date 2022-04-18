n=int(input("Enter a number to check it is amstrong or not:"))
s=0
num=n
while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n/10
if s==num:
    print("It is amstrong number.")
else:
    print("it is not amstrong number.")