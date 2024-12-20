# Khởi tạo ma trận 2D và số k
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
k = 2
# Cộng ma trận với số k
matrix_phep_cong_k = [[matrix[i][j] + k for j in range(len(matrix[i]))] for i in range(len(matrix))]
# Trừ ma trận với số k
matrix_phep_tru_k = [[matrix[i][j] - k for j in range(len(matrix[i]))] for i in range(len(matrix))]
# Nhân ma trận với số k
matrix_phep_nhan_k = [[matrix[i][j] * k for j in range(len(matrix[i]))] for i in range(len(matrix))]
# Chia ma trận với số k (cẩn thận với phép chia cho 0)
matrix_phep_chia_k = [[matrix[i][j] / k 
if k != 0 else "undefined" for j in range(len(matrix[i]))] for i in range(len(matrix))]
# In kết quả
print("Cộng ma trận với k:", matrix_phep_cong_k)
print("Trừ ma trận với k:", matrix_phep_tru_k)
print("Nhân ma trận với k:", matrix_phep_nhan_k)
print("Chia ma trận với k:", matrix_phep_chia_k)
