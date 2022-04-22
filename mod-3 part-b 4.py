lst=[i for i in input("Enter elments into list:").split()]
element=input("Enter the element you want to search:")
count=0
# for multiple index values.
for index,ele in enumerate(lst):
    if ele==element:
        print(index)
    else:
        pass

# for count

for i in lst:
    if i.startswith(element):
        count+=1
print("The count of a given number:",count)