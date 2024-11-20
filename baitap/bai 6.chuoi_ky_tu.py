# Nhập vào chuỗi ký tự
chuoi = "-12345"
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Kiểm tra chuỗi có phải là số âm không
if chuoi_sach.startswith("-"):
    # Kiểm tra nếu phần còn lại của chuỗi là các chữ số
    phan_con_lai = chuoi_sach[1:]
    la_so = True
    for ky_tu in phan_con_lai:
        if not ('0' <= ky_tu <= '9'):
            la_so = False
            break
    if la_so:
        print("Đây là số âm.")
    else:
        print("Đây không phải là số âm.")
else:
    print("Đây không phải là số âm.")
