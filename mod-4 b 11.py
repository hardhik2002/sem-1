str=input("Enter a string:")
sub_str=input("Enter a sub-string:")
count=0
for i in str:
    if i.startswith(sub_str):
        count+=1
    else:
        pass
print(count)
