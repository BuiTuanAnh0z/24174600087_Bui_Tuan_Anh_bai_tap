# Nhập vào tử số và mẫu số từ người dùng
Tu_so = int(input("Nhập vào tử số của phân số: "))                                                                              
Mau_so = int(input("Nhập vào mẫu số của phân số: "))

# Kiểm tra xem mẫu số có khác 0 không
if Mau_so == 0:
    print("Mẫu số không được bằng 0.")
else:
    # Hàm tìm UCLN
    gcd = 1  # Khởi tạo UCLN
    for i in range(1, min(abs(Tu_so), abs(Mau_so)) + 1):
        if Tu_so % i == 0 and Mau_so % i == 0:
            gcd = i  # Cập nhật UCLN

    # Tối giản phân số
    Tu_so_toi_gian = Tu_so // gcd
    Mau_so_toi_gian = Mau_so // gcd

    # Kết quả
    print(f"Phân số đã tối giản là: {Tu_so_toi_gian}/{Mau_so_toi_gian}")
