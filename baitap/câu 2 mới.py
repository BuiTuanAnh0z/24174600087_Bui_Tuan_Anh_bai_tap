# Nhập giá trị của n
n = int(input("Nhập n: "))
# Tính S1 = 1 + 2 + 3 + ... + n
S1 = 0
for i in range(1, n + 1):
    S1 += i
# Tính S2 = 1 * 2 * 3 * ... * (n - 1)
S2 = 1
for i in range(1, n):
    S2 *= i
# Tính S3 = 1 - 1/2 + 1/3 - 1/4 + ... + ((-1)**n) / n
S3 = 0
for i in range(1, n + 1):
    S3 += ((-1) ** (i + 1)) / i
# Tính S4 = sum(k / (k + 2)) từ k = 0 đến k = n
S4 = 0
for k in range(n + 1):
    S4 += k / (k + 2)
# In ra kết quả
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)