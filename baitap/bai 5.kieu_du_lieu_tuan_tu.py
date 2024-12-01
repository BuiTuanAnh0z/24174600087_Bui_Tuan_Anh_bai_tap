# Nhập vào kích thước ma trận n
n = int(input("Nhập vào kích thước ma trận n: "))

# Tạo ma trận đơn vị I
I = []
i = 0
while i < n:
    row = []
    j = 0
    while j < n:
        if i == j:
            row.append(1)  # Các phần tử trên đường chéo chính là 1
        else:
            row.append(0)  # Các phần tử còn lại là 0
        j += 1
    I.append(row)
    i += 1

# In ra ma trận I
print("Ma trận đơn vị I:")
for row in I:
    print(row)
