lst=[int(i) for i in input("Enter random elements into the list:").split()]
odd_lst=[]
even_lst=[]
for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("Even list:",even_lst)
print("odd list:",odd_lst)
