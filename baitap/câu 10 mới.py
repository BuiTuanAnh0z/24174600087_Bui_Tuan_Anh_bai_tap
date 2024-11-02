# Nhập vào hai số từ người dùng
a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))

# Khởi tạo UCLN
gcd = 1

# Tìm UCLN bằng cách kiểm tra các ước số
for i in range(1, min(a, b) + 1):  # Duyệt từ 1 đến số nhỏ hơn trong a và b
    if a % i == 0 and b % i == 0:  # Nếu i là ước của cả a và b
        gcd = i  # Cập nhật UCLN

# Kết quả
print(f"Ước chung lớn nhất của {a} và {b} là: {gcd}")
