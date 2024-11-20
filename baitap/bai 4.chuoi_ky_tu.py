# Nhập vào chuỗi ký tự
chuoi = "Xsn61ss@akdu271626s! 1231 12"
# Tách các ký tự và tạo lại chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu = chuoi.split()
chuoi_sach = "".join(cac_ky_tu)
# Khởi tạo các biến đếm
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
# Duyệt từng ký tự trong chuỗi
for ky_tu in chuoi_sach:
    # Kiểm tra nếu ký tự là chữ cái (A-Z hoặc a-z)
    if 'a' <= ky_tu <= 'z' or 'A' <= ky_tu <= 'Z':
        dem_chu += 1
    # Kiểm tra nếu ký tự là số (0-9)
    elif '0' <= ky_tu <= '9':
        dem_so += 1
    # Nếu không phải chữ và cũng không phải số, thì là ký tự đặc biệt
    else:
        dem_ky_tu_dac_biet += 1
# In kết quả
print(f"Số ký tự là chữ: {dem_chu}")
print(f"Số ký tự là số: {dem_so}")
print(f"Số ký tự là ký tự đặc biệt: {dem_ky_tu_dac_biet}")
