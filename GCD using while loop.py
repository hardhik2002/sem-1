"""
Write a programm to find GCD of the number.
"""
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
if n1>n2:
    divident=n1
    divisior=n2
else:
    divident=n2
    divisior=n1
while divisior!=0:
    reminder=divident%divisior
    divident=divisior
    divisior=reminder
print("The GCD is:",divident)