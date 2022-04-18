a,b,c=map(int,input("Enter the 3 values:").split())
delta=(b*b)-4*a*c
deno=2*a
if delta>0:
    print("Real Roots")
    root1=(-b+delta**0.5)/deno
    root2=(-b-delta**0.5)/deno
    print(root1,root2,end=",")
elif delta==0:
    print("Equal roots")
    root1=-b/deno
    print(root1,root1,end=",")
else:
    print("Imaginary roots")
