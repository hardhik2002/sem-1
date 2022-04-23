row=int(input("Enter row:"))
col=int(input("Enter col:"))
matrix1=[[int(input()) for i in range(col)] for j in range(row)]
print(matrix1)
matrix2=[[int(input()) for i in range(col)] for i in range(row)]
print(matrix2)
result=[[0 for i in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
print(result)