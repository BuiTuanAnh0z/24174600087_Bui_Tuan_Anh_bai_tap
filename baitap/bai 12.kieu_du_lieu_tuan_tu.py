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

# Nhập tên sinh viên cần xóa
ten_xoa = input("Nhập tên sinh viên cần xóa: ")

# Xóa sinh viên trong danh sách
ds_sinh_vien = [sinh_vien for sinh_vien in ds_sinh_vien if ten_xoa not in sinh_vien]

# In danh sách sinh viên sau khi xóa
print("Danh sách sinh viên còn lại:")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"Tên: {ten}, Điểm tổng kết: {diem}")
