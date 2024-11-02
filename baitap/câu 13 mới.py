# Nhập vào số từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem n có phải là số nguyên dương không
if n < 1:
    print("Vui lòng nhập một số nguyên dương.")
else:
    factors = []  # Danh sách để lưu các thừa số nguyên tố
    original_n = n  # Lưu lại giá trị ban đầu của n để in ra sau

    # Tìm các thừa số nguyên tố
    for i in range(2, n + 1):
        while n % i == 0:  # Nếu i là ước của n
            factors.append(i)  # Thêm i vào danh sách thừa số
            n //= i  # Chia n cho i

    # Kết quả
    if factors:
        print(f"Các thừa số nguyên tố của {original_n} là: ", end="")
        print("*".join(map(str, factors)))  # In các thừa số đã tìm được
    else:
        print(f"{original_n} không có thừa số nguyên tố.")
