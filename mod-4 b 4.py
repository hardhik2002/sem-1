str=input("Enter a string:")
sub_str=input("Enter a sub string:")
for i in range(len(str)):
    if str.startswith(sub_str,i):
        print(i)
