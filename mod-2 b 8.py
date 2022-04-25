pos,neg,zero=0,0,0
n=int(input("Enter numbers:"))
while n!=-1:
    if n>0:
        pos+=1
    elif n<0:
        neg+=1
    else:
        zero+=1
    n=int(input("Enter number:"))
print(pos,neg,zero)