# Nhập vào chuỗi ký tự
chuoi = "Xsn61ssakdu271626sABCabc!"
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Khởi tạo các biến đếm
dem_chu_hoa = 0
dem_chu_thuong = 0
# Duyệt từng ký tự trong chuỗi
for ky_tu in chuoi_sach:
    # Kiểm tra nếu ký tự là chữ cái viết hoa (A-Z)
    if 'A' <= ky_tu <= 'Z':
        dem_chu_hoa += 1
    # Kiểm tra nếu ký tự là chữ cái viết thường (a-z)
    elif 'a' <= ky_tu <= 'z':
        dem_chu_thuong += 1
# In kết quả
print(f"Số chữ cái viết hoa: {dem_chu_hoa}")
print(f"Số chữ cái viết thường: {dem_chu_thuong}")
