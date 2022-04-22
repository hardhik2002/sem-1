lst=[i for i in input("Enter elements into list:").split()]
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
    else:
        pass
print(lst2)