# Danh sách sinh viên ban đầu
ds_sinh_vien = []
# Hàm tính điểm trung bình của sinh viên
def tinh_diem_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
# Menu chương trình
while True:
    print("\n----- MENU -----")
    print("1. Xem danh sách sinh viên")
    print("2. Nhập thông tin sinh viên mới vào danh sách")
    print("3. Chỉnh sửa thông tin sinh viên ứng với mã sinh viên")
    print("4. Xóa thông tin sinh viên ứng với mã sinh viên")
    print("5. Thoát chương trình")
    lua_chon = input("Chọn chức năng: ")
    if lua_chon == "1":
        print("\nDanh sách sinh viên:")
        if not ds_sinh_vien:
            print("Danh sách trống!")
        else:
            for sinh_vien in ds_sinh_vien:
                print(f"Mã sinh viên: {sinh_vien['ma_sv']}, Họ tên: {sinh_vien['ho_dem']} {sinh_vien['ten']}, "
                      f"Điểm toán: {sinh_vien['diem_toan']}, Điểm lý: {sinh_vien['diem_ly']}, "
                      f"Điểm hóa: {sinh_vien['diem_hoa']}, Điểm trung bình: {sinh_vien['diem_trung_binh']}")
    elif lua_chon == "2":
        ma_sv = input("Nhập mã sinh viên: ")
        ho_dem = input("Nhập họ đệm: ")
        ten = input("Nhập tên: ")
        diem_toan = float(input("Nhập điểm toán: "))
        diem_ly = float(input("Nhập điểm lý: "))
        diem_hoa = float(input("Nhập điểm hóa: "))
        diem_trung_binh = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
        sinh_vien_moi = {
            "ma_sv": ma_sv,
            "ho_dem": ho_dem,
            "ten": ten,
            "diem_toan": diem_toan,
            "diem_ly": diem_ly,
            "diem_hoa": diem_hoa,
            "diem_trung_binh": diem_trung_binh
        }
        ds_sinh_vien.append(sinh_vien_moi)
        print("Đã thêm sinh viên mới vào danh sách.")
    elif lua_chon == "3":
        ma_sv_sua = input("Nhập mã sinh viên cần sửa: ")
        sinh_vien_sua = False
        for sinh_vien in ds_sinh_vien:
            if sinh_vien["ma_sv"] == ma_sv_sua:
                sinh_vien_sua = True
                sinh_vien["ho_dem"] = input("Nhập họ đệm mới: ")
                sinh_vien["ten"] = input("Nhập tên mới: ")
                sinh_vien["diem_toan"] = float(input("Nhập điểm toán mới: "))
                sinh_vien["diem_ly"] = float(input("Nhập điểm lý mới: "))
                sinh_vien["diem_hoa"] = float(input("Nhập điểm hóa mới: "))
                sinh_vien["diem_trung_binh"] = tinh_diem_trung_binh(sinh_vien["diem_toan"], sinh_vien["diem_ly"], sinh_vien["diem_hoa"])
                print("Đã sửa thông tin sinh viên.")
                break
        if not sinh_vien_sua:
            print("Không tìm thấy sinh viên với mã số này.")
    elif lua_chon == "4":
        ma_sv_xoa = input("Nhập mã sinh viên cần xóa: ")
        sinh_vien_xoa = False  
        for sinh_vien in ds_sinh_vien:
            if sinh_vien["ma_sv"] == ma_sv_xoa:
                ds_sinh_vien.remove(sinh_vien)
                sinh_vien_xoa = True
                print("Đã xóa thông tin sinh viên.")
                break
        if not sinh_vien_xoa:
            print("Không tìm thấy sinh viên với mã số này.")
    elif lua_chon == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
