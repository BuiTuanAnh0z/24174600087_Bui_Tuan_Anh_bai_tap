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
# Nhập hai hàng i và j cần hoán đổi
i = int(input("Nhập chỉ số hàng i (từ 0 đến m-1): "))
j = int(input("Nhập chỉ số hàng j (từ 0 đến m-1): "))
# Hoán đổi hai hàng i và j
if 0 <= i < m and 0 <= j < m:
    A[i], A[j] = A[j], A[i]
else:
    print("Chỉ số hàng không hợp lệ.")
# In ma trận sau khi hoán đổi
print("Ma trận A sau khi hoán đổi:")
for row in A:
    print(row)
