'''
These algorithms are from reema thareeja book.
'''
# 4.1

n=int(input("Enter a number:"))
print("The number after incriment:",n+1) if n>0 else print("You entered negative value.")

# 4.2
chr=input("Enter anything:")
if chr.isalpha():
    print("user entered character.")
if chr.isdigit():
    print("user entered digit")
if chr.isspace():
    pprint("The entered is a space.")

# 4.3
age=int(input("Enter age:"))
if age>=18:
    print("You are eligible for vote.")
else:
    r_age=18-age
    print("You need to wait {} years to get vote.".format(r_age))

# 4.4
num_lst=[int(i) for i in input("Enter numbers to get largest from  that:").split()]
print("The largest number is:",max(num_lst))
# altarnate
a,b=map(int,input("Enter two numbers:").split())
print(a) if a>b else print(b)

# 4.5
n=int(input("Enter the number to know wether it is even or not:" ))
print("even") if n%2==0 else print("odd")

# 4.6
ch=input("Enter a charecter:")
if (ch>="A" and ch<="Z"):

        ch=ch.lower()
        print(ch)
else:
        ch=ch.upper()
        print(ch)

# 4.7
sex=input("Enter male or female:").lower()
salary=int(input("Enter your salary:"))
if sex=="m":
    bonus=0.05*salary
else:
    bonus=0.10*salary
if salary<10000:
    amt_to_paid=0.02*(salary+bonus)
else:
    amt_to_paid=salary+bonus
print("salary:",salary)
print("Bonus:",bonus)
print("The ammount to be paid:",amt_to_paid)





