# Nhập một số từ người dùng
n = int(input("Nhập một số nguyên dương: "))

# Kiểm tra nếu số nhỏ hơn 2 thì không phải là số nguyên tố
if n < 2:
    print(f"{n} không phải là số nguyên tố.")
else:
    # Giả sử n là số nguyên tố
    is_prime = True
    # Kiểm tra các ước từ 2 đến căn bậc hai của n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    # In kết quả
    if is_prime:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
