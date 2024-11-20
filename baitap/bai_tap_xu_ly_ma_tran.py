matrix_a = [[0,1,2],
            [4,5,6],
            [7,8,9]]
n = 8
#Nhân ma trận a với n
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * n

print(matrix_a)
