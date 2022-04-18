n,m=map(int,input("Enter range:").split())
for i in range(n,m+1):
    print(i," is even.") if i%2==0 else print(i," is odd.")
