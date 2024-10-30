# Nhập các hệ số từ bàn phím
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))

# Tính định thức D
D = a1 * b2 - a2 * b1

# Kiểm tra các trường hợp
if D != 0:
    # Tính định thức Dx và Dy
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    # Tính nghiệm
    x = Dx / D
    y = Dy / D
    print(f"Hệ phương trình có nghiệm duy nhất: x = {x}, y = {y}")
elif D == 0:
    # Nếu D = 0, kiểm tra thêm để xác định loại hệ
    if (c1 * b2 == c2 * b1) and (a1 * c2 == a2 * c1):
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
