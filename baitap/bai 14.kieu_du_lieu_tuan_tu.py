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
# Nhập tên sinh viên cần sửa thông tin
ten_sua = input("Nhập tên sinh viên cần sửa thông tin: ")
# Tìm và sửa thông tin sinh viên
sinh_vien_sua = False
for sinh_vien in ds_sinh_vien:
    if ten_sua in sinh_vien:
        sinh_vien_sua = True
        diem_moi = float(input(f"Nhập điểm tổng kết mới cho sinh viên {ten_sua}: "))
        sinh_vien[ten_sua] = diem_moi  # Cập nhật điểm mới
        print(f"Đã sửa thông tin sinh viên {ten_sua}")
        break
if not sinh_vien_sua:
    print("Sinh viên không có trong danh sách")
# In danh sách sinh viên sau khi sửa
print("Danh sách sinh viên:")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"Tên: {ten}, Điểm tổng kết: {diem}")
