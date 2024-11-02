# Nhập vào hai số từ người dùng
a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))

# Tìm UCLN của a và b
gcd = 1  # Khởi tạo UCLN
for i in range(1, min(a, b) + 1):  # Duyệt từ 1 đến số nhỏ hơn trong a và b
    if a % i == 0 and b % i == 0:  # Nếu i là ước của cả a và b
        gcd = i  # Cập nhật UCLN

# Tính BCNN
lcm = (a * b) // gcd  # Công thức tính BCNN

# Kết quả
print(f"Bội chung nhỏ nhất của {a} và {b} là: {lcm}")
