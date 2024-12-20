
def nhap_thong_tin_mat_hang():
    """Nhập thông tin một mặt hàng từ bàn phím."""
    ma_hang = input("Nhập mã hàng: ")
    ten_hang = input("Nhập tên hàng: ")
    don_vi = input("Nhập đơn vị tính: ")
    try:
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
    except ValueError:
        print("Giá trị đơn giá và số lượng phải là số!")
        return None
    thanh_tien = don_gia * so_luong
    thue_vat = thanh_tien * 0.1
    return ma_hang, ten_hang, don_vi, don_gia, so_luong, thanh_tien, thue_vat
def xem_danh_sach_mat_hang(danh_sach_mat_hang):
    """Hiển thị danh sách các mặt hàng."""
    if not danh_sach_mat_hang:
        print("Danh sách mặt hàng hiện đang trống.")
        return
    print("Danh sách mặt hàng:")
    print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "Mã hàng", "Tên hàng", "Đơn vị", "Đơn giá", "Số lượng", "Thành tiền", "Thuế VAT"
    ))
    for hang in danh_sach_mat_hang:
        print("{:<10} {:<20} {:<10} {:<10} {:<10} {:<10.2f} {:<10.2f}".format(*hang))

def tim_kiem_mat_hang(danh_sach_mat_hang, ma_hang):
    """Tìm kiếm mặt hàng theo mã hàng."""
    for i, hang in enumerate(danh_sach_mat_hang):
        if hang[0] == ma_hang:
            return i
    return -1

def xoa_mat_hang(danh_sach_mat_hang, ma_hang):
    """Xóa mặt hàng theo mã hàng."""
    vi_tri = tim_kiem_mat_hang(danh_sach_mat_hang, ma_hang)
    if vi_tri != -1:
        del danh_sach_mat_hang[vi_tri]
        print("Xóa mặt hàng thành công!")
    else:
        print("Không tìm thấy mặt hàng để xóa.")

def chinh_sua_mat_hang(danh_sach_mat_hang, ma_hang):
    """Chỉnh sửa thông tin mặt hàng theo mã hàng."""
    vi_tri = tim_kiem_mat_hang(danh_sach_mat_hang, ma_hang)
    if vi_tri != -1:
        thong_tin_moi = nhap_thong_tin_mat_hang()
        if thong_tin_moi:
            danh_sach_mat_hang[vi_tri] = thong_tin_moi
            print("Chỉnh sửa mặt hàng thành công!")
        else:
            print("Nhập thông tin mới không hợp lệ.")
    else:
        print("Không tìm thấy mặt hàng để chỉnh sửa.")

def sap_xep_theo_ten(danh_sach_mat_hang):
    """Sắp xếp danh sách mặt hàng theo tên tăng dần."""
    danh_sach_mat_hang.sort(key=lambda x: x[1])
if __name__ == "__main__":
    danh_sach_mat_hang = []
    while True:
        print("\nChương trình quản lý hàng hóa")
        print("1. Xem danh sách mặt hàng")
        print("2. Nhập thông tin mặt hàng")
        print("3. Tìm kiếm và xóa mặt hàng")
        print("4. Tìm kiếm và chỉnh sửa mặt hàng")
        print("5. Sắp xếp danh sách theo tên")
        print("6. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            xem_danh_sach_mat_hang(danh_sach_mat_hang)
        elif lua_chon == '2':
            thong_tin_moi = nhap_thong_tin_mat_hang()
            if thong_tin_moi:
                danh_sach_mat_hang.append(thong_tin_moi)
        elif lua_chon == '3':
            ma_hang = input("Nhập mã hàng cần xóa: ")
            xoa_mat_hang(danh_sach_mat_hang, ma_hang)
        elif lua_chon == '4':
            ma_hang = input("Nhập mã hàng cần chỉnh sửa: ")
            chinh_sua_mat_hang(danh_sach_mat_hang, ma_hang)
        elif lua_chon == '5':
            sap_xep_theo_ten(danh_sach_mat_hang)
            print("Danh sách đã được sắp xếp theo tên.")
        elif lua_chon == '6':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
            if not ma_hang :
                raise ValueError("Mã hàng ko đc để trống!")
            if not danh_sach_mat_hang :
                raise ValueError("Danh sách mặt hàng ko đc để trống!")
