ds_so = []
while True:
    n = input("Nhập vào số phần tử n trong danh sách: ")
    if n.lstrip('-').isdigit() == False:  # Kiểm tra cả số âm
        print("Yêu cầu nhập lại số nguyên (có thể là số âm)!!")
    else:
        n = int(n)
        break
for i in range(n):
    while True:
        so = input(f"Nhập giá trị số thứ {i + 1}: ")
        if not (so.lstrip('-').replace('.', '', 1).isdigit() and so.count('.') <= 1):  # Kiểm tra số thực có dấu âm
            print("Yêu cầu nhập vào số thực!!")
        else:
            so = float(so)
            break
    ds_so.append(so)
tong = sum(ds_so)
print(f"Tổng các số vừa nhập: {tong}")


