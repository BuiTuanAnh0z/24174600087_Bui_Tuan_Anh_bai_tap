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
# In danh sách sinh viên với định dạng yêu cầu
print(f"{'Ten':<10} {'Diem'}")
for sinh_vien in ds_sinh_vien:
    for ten, diem in sinh_vien.items():
        print(f"{ten:<10} {diem}")
