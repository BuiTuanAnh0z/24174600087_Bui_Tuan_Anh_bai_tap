# Nhập ba cạnh a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện để tạo thành tam giác
if a + b > c and a + c > b and b + c > a:
    # Nếu thỏa mãn điều kiện tam giác, kiểm tra loại tam giác

    # Kiểm tra tam giác đều
    if a == b == c:
        print("Đây là tam giác đều.")
    
    # Kiểm tra tam giác cân
    elif a == b or a == c or b == c:
        # Nếu là tam giác cân, kiểm tra thêm xem có phải là tam giác vuông cân không
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Đây là tam giác vuông cân.")
        else:
            print("Đây là tam giác cân.")

    # Kiểm tra tam giác vuông
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông.")

    # Nếu không phải tam giác đều, cân, hoặc vuông thì là tam giác thường
    else:
        print("Đây là tam giác thường.")
else:
    print("Ba cạnh a, b, c không phải là ba cạnh của một tam giác.")
