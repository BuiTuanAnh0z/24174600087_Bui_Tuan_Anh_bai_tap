# Nhập vào số từ người dùng
n = int(input("Nhập vào một số nguyên dương: "))

# Biến để kiểm tra
is_perfect_square = False

# Kiểm tra từ 1 đến n xem có số nào là căn bậc hai của n không
for i in range(1, n + 1):
    if i * i == n:
        is_perfect_square = True
        break  # Nếu tìm thấy thì thoát khỏi vòng lặp

# Kết quả
if is_perfect_square:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
