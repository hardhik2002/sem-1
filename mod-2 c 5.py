row=int(input("Enter the number off rows:"))
col=int(input("Enter the number off colums:"))
for i in range(1,row+1):
    for j in range(1,col+1):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()