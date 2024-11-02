# Nhập vào số hàng cho tam giác Pascal
n = int(input("Nhập vào số hàng cho tam giác Pascal: "))

# Khởi tạo tam giác Pascal
tam_giac_Pascal = []

for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)  # Các phần tử đầu và cuối mỗi hàng là 1
        else:
            row.append(tam_giac_Pascal[i - 1][j - 1] + tam_giac_Pascal[i - 1][j])  # Tính giá trị từ hai phần tử phía trên
    tam_giac_Pascal.append(row)

# In tam giác Pascal
print("Tam giác Pascal:")
for row in tam_giac_Pascal:
    print(" " * (n - len(row)), end="")  # Căn giữa
    print(" ".join(map(str, row)))
