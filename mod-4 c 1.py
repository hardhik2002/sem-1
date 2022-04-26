def l_u(str):
    r=""
    for i in str:
        if i.islower():
            r+=i
    for i in str:
        if i.isupper():
            r+=i
    print(r)
str=input("Enter a string:")
l_u(str)