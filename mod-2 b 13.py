m=int(input())
n=int(input())
eve=0
odd=0
for i in range(m,n+1):
    if i%2==0:
        eve+=1
    else:
        odd+=1
print(eve)
print(odd)

