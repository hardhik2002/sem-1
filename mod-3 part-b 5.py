lst1=["Hardhik","Harsha"]
lst2=["Reddy","Reddy"]
n_lst=[]
for i in lst1:
    for j in lst2:
        n_lst.append(i+j)
        break
print(n_lst)