# program 4.14 page no.146
m1,m2,m3,m4=map(int,input("Enter four subjects marks:").split())
avg=(m1+m2+m3+m4)/4
print("The average of 4 subjects is:",avg)
if avg<=100:
    if (avg>75):
        print("distinction")
    elif (avg>=60 and avg<75):
        print("First class")
    elif (avg>=50 and avg<60):
        print("Second class")
    elif (avg>=40 and avg<50):
        print("Third class")
    else:
        print("Fail")
else:
    print("Extended range")
