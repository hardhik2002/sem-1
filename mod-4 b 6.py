def both_ends(n):
    if len(n)<2:
        return n
    return n[0:2]+n[-2:]
n=input("Enter a string:")
print(both_ends(n))