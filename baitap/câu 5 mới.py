# Nhập một số từ người dùng
n = int(input("Nhập một số nguyên dương: "))

# Tính tổng các ước của n (ngoại trừ n)
tong_cac_uoc_so = 0
for i in range(1, n):
    if n % i == 0:
        tong_cac_uoc_so += i

# Kiểm tra nếu tổng các ước bằng n
if tong_cac_uoc_so == n:
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")
