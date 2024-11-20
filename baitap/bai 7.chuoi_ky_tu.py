# Nhập vào chuỗi ký tự
chuoi = "-123.45"
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Kiểm tra chuỗi có phải là số thập phân không
dau_dau = chuoi_sach.startswith("-")
chuoi_sach = chuoi_sach[1:] if dau_dau else chuoi_sach
# Kiểm tra nếu chuỗi có đúng một dấu chấm và phần còn lại chỉ là số
dau_cham = False
la_so = True
for ky_tu in chuoi_sach:
    if ky_tu == ".":
        if dau_cham:  # Nếu đã có dấu chấm, không phải số thập phân hợp lệ
            la_so = False
            break
        dau_cham = True
    elif not ('0' <= ky_tu <= '9'):
        la_so = False
        break
# In kết quả
if la_so and dau_cham:
    print("Đây là số thập phân.")
else:
    print("Đây không phải là số thập phân.")

