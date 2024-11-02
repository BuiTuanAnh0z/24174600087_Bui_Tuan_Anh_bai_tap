# Nhập vào lựa chọn chuyển đổi
choice = input("Bạn muốn chuyển đổi từ (1) Hệ cơ số 10 sang hệ cơ số 2 hay (2) Hệ cơ số 2 sang hệ cơ số 10? (Nhập 1 hoặc 2): ")

if choice == '1':
    # Chuyển từ hệ cơ số 10 sang hệ cơ số 2
    so_thap_phan = int(input("Nhập vào số nguyên trong hệ cơ số 10: "))
    so_nhi_phan = ""  # Khởi tạo chuỗi để lưu số nhị phân

    if so_thap_phan == 0:
       so_nhi_phan = "0"
    else:
        while so_thap_phan > 0:
            so_nhi_phan = str(so_thap_phan % 2) + so_nhi_phan  # Lấy phần dư và thêm vào chuỗi
            so_thap_phan //= 2  # Chia cho 2

    print(f"Số trong hệ cơ số 2 là: {so_nhi_phan}")

elif choice == '2':
    # Chuyển từ hệ cơ số 2 sang hệ cơ số 10
    so_nhi_phan = input("Nhập vào số nhị phân: ")
    so_thap_phan = 0  # Khởi tạo biến để lưu số thập phân

    for i in range(len(so_nhi_phan)):
       so_thap_phan += int(so_nhi_phan[-(i + 1)]) * (2 ** i)  # Tính giá trị thập phân

    print(f"Số trong hệ cơ số 10 là: {so_thap_phan}")

else:
    print("Lựa chọn không hợp lệ. Vui lòng nhập 1 hoặc 2.")
