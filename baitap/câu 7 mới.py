# Nhập vào n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem số nguyên tố có thể được tìm thấy
if n < 2:
    print("Không có số nguyên tố nhỏ hơn", n)
else:
    print(f"Các số nguyên tố nhỏ hơn {n} là:")
    # Duyệt qua các số từ 2 đến n-1
    for num in range(2, n):
        is_prime = True  # Giả định num là số nguyên tố
        # Kiểm tra xem num có phải là số nguyên tố hay không
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False  # num không phải là số nguyên tố
                break
        # Nếu là số nguyên tố, in ra
        if is_prime:
            print(num)
