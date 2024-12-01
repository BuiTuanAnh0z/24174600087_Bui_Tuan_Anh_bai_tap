# Nhập vào kích thước ma trận m và n
m = int(input("Nhập vào số hàng m: "))
n = int(input("Nhập vào số cột n: "))

# Tạo ma trận K chỉ chứa số 0
K = []
i = 0
while i < m:
    row = []
    j = 0
    while j < n:
        row.append(0)
        j += 1
    K.append(row)
    i += 1

# In ra ma trận K
print("Ma trận K:")
for row in K:
    print(row)
