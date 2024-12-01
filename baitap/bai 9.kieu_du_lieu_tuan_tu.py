# Nhập kích thước ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# Nhập ma trận A
A = []
print("Nhập ma trận A:")
i = 0
while i < m:
    row = list(map(int, input().split()))
    A.append(row)
    i += 1

# Nhập ma trận B
B = []
print("Nhập ma trận B:")
i = 0
while i < m:
    row = list(map(int, input().split()))
    B.append(row)
    i += 1

# Nhập số k
k = int(input("Nhập số k để tính tích với ma trận A: "))

# Tính tổng hai ma trận A và B
print("Tổng hai ma trận A và B:")
i = 0
while i < m:
    j = 0
    while j < n:
        print(A[i][j] + B[i][j], end=" ")
        j += 1
    print()
    i += 1

# Tính hiệu hai ma trận A và B
print("Hiệu hai ma trận A và B:")
i = 0
while i < m:
    j = 0
    while j < n:
        print(A[i][j] - B[i][j], end=" ")
        j += 1
    print()
    i += 1

# Tính tích ma trận A với số k
print(f"Tích của ma trận A với số {k}:")
i = 0
while i < m:
    j = 0
    while j < n:
        print(A[i][j] * k, end=" ")
        j += 1
    print()
    i += 1

# Tính tích của hai ma trận A và B
print("Tích của ma trận A và B:")
if m == n:
    # Tích ma trận chỉ có thể thực hiện khi số cột của ma trận A bằng số hàng của ma trận B
    result = [[0] * n for _ in range(m)]
    i = 0
    while i < m:
        j = 0
        while j < n:
            k = 0
            while k < n:
                result[i][j] += A[i][k] * B[k][j]
                k += 1
            print(result[i][j], end=" ")
            j += 1
        print()
        i += 1
else:
    print("Không thể tính tích vì số cột của A không bằng số hàng của B.")

# Tính ma trận đối xứng của ma trận A
print("Ma trận đối xứng của ma trận A:")
i = 0
while i < m:
    j = 0
    while j < n:
        print(A[j][i], end=" ")  # Hoán đổi chỉ số hàng và cột
        j += 1
    print()
    i += 1
