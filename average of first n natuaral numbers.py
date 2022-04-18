n=int(input("Enter range:"))
s=0
avg=0.0
for i in range(1,n+1):
    s=s+i
avg=s/i
print("The average of first n natural numbers are:",avg)
# sum of first n natural numbers:
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum is:",sum)