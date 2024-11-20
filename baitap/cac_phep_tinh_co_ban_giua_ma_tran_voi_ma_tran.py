# Khởi tạo hai ma trận 2D cùng kích thước
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# Gọi hàng là i, cột là j
# Cộng ma trận với nhau
matrix_phep_cong = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
# Trừ ma trận với nhau
matrix_phep_tru = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
# Nhân ma trận với nhau (phép nhân từng phần tử)
matrix_phep_nhan = [[matrix1[i][j] * matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
# Chia ma trận với nhau (cẩn thận với phép chia cho 0)
matrix_phep_chia = [[matrix1[i][j] / matrix2[i][j] if matrix2[i][j] != 0 else "undefined" for j in range(len(matrix1[i]))] for i in range(len(matrix1))]
# In kết quả
print("Cộng ma trận với nhau:", matrix_phep_cong)
print("Trừ ma trận với nhau:", matrix_phep_tru)
print("Nhân ma trận với nhau:", matrix_phep_nhan)
print("Chia ma trận với nhau:", matrix_phep_chia)
