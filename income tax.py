# program 4.12 page number: 145
min1=150001
max1=300000
rate1=0.10
min2=300001
max2=500000
rate2=0.20
min3=500001
rate3=0.30
income=int(input("Enter your annual income:"))
taxable_income=income-150000
if taxable_income<=0:
    print("No tax")
elif (taxable_income>=min1 and taxable_income<=max1):
    print("The tax is:",(taxable_income-min1)*rate1)
elif taxable_income>=min2 and taxable_income<=max2:
    print("income tax is:",(taxable_income-min2)*rate2)
else:
    print("income tax is:",(taxable_income-min3)*rate3)
