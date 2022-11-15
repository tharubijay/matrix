

r = int(input("enter row : "))
c = int(input("enter columns : "))
matrix = []

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter Value = ")))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()