# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
# Nhập ma trận A
A = []
print("Nhập ma trận A:")
i = 0
while i < m:
    print(f"Nhập hàng thứ {i + 1} (nhập {n} số, cách nhau bởi khoảng trắng):")
    row = list(map(int, input().split()))
    A.append(row)
    i += 1
# Nhập hai cột i và j cần hoán đổi
i = int(input("Nhập chỉ số cột i (từ 0 đến n-1): "))
j = int(input("Nhập chỉ số cột j (từ 0 đến n-1): "))

# Hoán đổi hai cột i và j
if 0 <= i < n and 0 <= j < n:
    row_index = 0
    while row_index < m:
        A[row_index][i], A[row_index][j] = A[row_index][j], A[row_index][i]
        row_index += 1
else:
    print("Chỉ số cột không hợp lệ.")
# In ma trận sau khi hoán đổi
print("Ma trận A sau khi hoán đổi:")
for row in A:
    print(row)
