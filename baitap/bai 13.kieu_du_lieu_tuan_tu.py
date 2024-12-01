# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên n: "))
# Danh sách chứa thông tin sinh viên
ds_sinh_vien = []
# Nhập thông tin cho từng sinh viên
for i in range(n):
    ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
    diem = float(input(f"Nhập điểm tổng kết của sinh viên {ten}: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
# Nhập tên sinh viên cần thêm
ten_them = input("Nhập tên sinh viên cần thêm: ")
# Kiểm tra xem sinh viên đã tồn tại hay chưa
sinh_vien_ton_tai = False
for sinh_vien in ds_sinh_vien:
    if ten_them in sinh_vien:
        sinh_vien_ton_tai = True
        break
if sinh_vien_ton_tai:
    print("Thông tin sinh viên đã tồn tại")
else:
    diem_them = float(input(f"Nhập điểm tổng kết của sinh viên {ten_them}: "))
    thong_tin_sinh_vien_moi = {ten_them: diem_them}
    ds_sinh_vien.append(thong_tin_sinh_vien_moi)
    print("Đã thêm sinh viên")
# In danh sách sinh viên sau khi thêm
print("Danh sách sinh viên:")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"Tên: {ten}, Điểm tổng kết: {diem}")
