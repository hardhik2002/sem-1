# 1/2 + 2/3 +.....+n/(n+1)
n=int(input("Enter a number:"))
s=0.0
for i in range(1,n+1):
    f=float(i)/(i+1)
    s=s+f
print("The result is:",s)
# 1/1 + 2**2/2 +.....+n**n/n
for i in range(1,n+1):
    f=float(i**i)/i
    s=s+f
print("The result is:",s)

