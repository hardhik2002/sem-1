"""
1
2 2
3 3 3
4 4 4 4
"""
n=int(input("Enter number of rows:"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()
    