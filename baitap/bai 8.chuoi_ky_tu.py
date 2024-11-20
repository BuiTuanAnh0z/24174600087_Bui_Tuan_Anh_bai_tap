# Nhập vào hai xâu ký tự
str_1 = "Hello world"
str_2 = "world"
# Tạo lại các chuỗi đã loại bỏ khoảng trắng thừa
cac_ky_tu_1 = str_1.split()
str_1_sach = "".join(cac_ky_tu_1)
cac_ky_tu_2 = str_2.split()
str_2_sach = "".join(cac_ky_tu_2)
# Kiểm tra xem str_2 có nằm trong str_1 hay không
found_in_str_1 = False
for i in range(len(str_1_sach) - len(str_2_sach) + 1):
    if str_1_sach[i:i + len(str_2_sach)] == str_2_sach:
        found_in_str_1 = True
        break
# Kiểm tra xem str_1 có nằm trong str_2 hay không (ngược lại)
found_in_str_2 = False
for i in range(len(str_2_sach) - len(str_1_sach) + 1):
    if str_2_sach[i:i + len(str_1_sach)] == str_1_sach:
        found_in_str_2 = True
        break
# In kết quả
if found_in_str_1:
    print(f"'{str_2}' nằm trong '{str_1}'")
else:
    print(f"'{str_2}' không nằm trong '{str_1}'")

if found_in_str_2:
    print(f"'{str_1}' nằm trong '{str_2}'")
else:
    print(f"'{str_1}' không nằm trong '{str_2}'")
