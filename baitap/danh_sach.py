# Khởi tạo ma trận 2D và số k
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 2
# Cộng ma trận với số k
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] + k
# Trừ ma trận với số k
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] - k
# Nhân ma trận với số k
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = matrix_a[hang][cot] * k
# Chia ma trận với số k (cẩn thận với phép chia cho 0)
for hang in range(len(matrix_a)):
    for cot in range(len(matrix_a[hang])):
        matrix_a[hang][cot] = [matrix_a[hang][cot] / k  if k != 0 else "Không xác định"
        for hang in range(len(matrix_a[hang])) 
        for cot in range(len(matrix_a[cot]))]
print("Cộng ma trận với k:",matrix_a)
print("Trừ ma trận với k:",matrix_a )
print("Nhân ma trận với k:",matrix_a )
print("Chia ma trận với k:",matrix_a)