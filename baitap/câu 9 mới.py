# Nhập vào n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem số chính phương có thể được tìm thấy
if n < 1:
    print("Không có số chính phương nhỏ hơn", n)
else:
    print(f"Các số chính phương nhỏ hơn {n} là:")
    
    # Duyệt qua các số từ 1 đến n-1
    for i in range(1, n):
        perfect_square = i * i  # Tính bình phương của i
        if perfect_square < n:
            print(perfect_square)  # In ra số chính phương
