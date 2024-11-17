# Nhập vào chuỗi ký tự
chuoi = "Xsn61ssakdu271626s  1231  12"
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Tạo danh sách chứa các số và các ký tự riêng biệt
so = "".join([ky_tu for ky_tu in chuoi_sach if ky_tu.isdigit()])
chuoi_con_lai = "".join([ky_tu for ky_tu in chuoi_sach if not ky_tu.isdigit()])
# Dồn các số sang bên trái và các ký tự sang bên phải
chuoi_moi = so + chuoi_con_lai
# In kết quả
print(f"Kết quả chuỗi mới:{chuoi_moi}")
