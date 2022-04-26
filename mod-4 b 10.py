str=input("Enter a string:")
sub_str=input("Enter a substring:")
index=-1
for i in str:
    index+=1
    if i in sub_str:
        print("It is present at:",index)