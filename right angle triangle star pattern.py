for i in range(1,(int(input("Enter range:")))+1):
    print("* "*i)
# altarnetive 
row=int(input("Enter No.off rows:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
