# Nhập số hàng và số cột của ma trận
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
# Nhập ma trận A
A = []
i = 0
while i < m:
    print(f"Nhập hàng thứ {i + 1} (nhập {n} số, cách nhau bởi khoảng trắng):")
    row = list(map(int, input().split()))
    A.append(row)
    i += 1
# In ra số hàng m
print("Số hàng của ma trận A là:", m)
