lst=[int(i) for i in input("Enter both positive and negative numbers:").split()]
new_list=[]
for i in lst:
    if i>0:
        new_list.append(i)
    else:
        pass
print(new_list)