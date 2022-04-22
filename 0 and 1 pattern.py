"""
01010
01010
01010
01010
"""
row=int(input("Enter the rows:"))
col=int(input("Enter the colums:"))
for i in range(1,row+1):
    for j in range(1,col+1):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
