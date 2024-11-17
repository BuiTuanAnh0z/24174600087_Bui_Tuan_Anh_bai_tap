# Nhập vào chuỗi ký tự
chuoi = "  0010  "
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Kiểm tra xem có phải số nhị phân không
la_nhi_phan = True
for ky_tu in chuoi_sach:
    if ky_tu != "0" and ky_tu != "1":
        la_nhi_phan = False
        break
# Xử lý và in kết quả
if la_nhi_phan:
    # Chuyển chuỗi nhị phân sang số thập phân
    so_thap_phan = int(chuoi_sach, 2)
    print(f"{chuoi_sach} là số nhị phân, chuyển sang thập phân: {so_thap_phan}")
else:
    print(f"{chuoi_sach} không phải là số nhị phân")
