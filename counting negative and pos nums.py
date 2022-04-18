"""
write a program to read the numbers until -1 is encountered.Also count negative,positive and
zeroes entered by the user.
"""
neg = pos = zero = 0
print(
    "Enter -1 to exit from the loop...."
)
while (1):
    num=int(input("Enter a number:"))
    if num==-1:
        break
    elif num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
print("No.off positives:",pos)
print("no.off negatives:",neg)
print("No.off zeroes:",zero)