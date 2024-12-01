# Nhập tọa độ các đỉnh
print("Nhập tọa độ điểm A:")
x1, y1 = float(input("x1: ")), float(input("y1: "))
print("Nhập tọa độ điểm B:")
x2, y2 = float(input("x2: ")), float(input("y2: "))
print("Nhập tọa độ điểm C:")
x3, y3 = float(input("x3: ")), float(input("y3: "))

# Tính các độ dài cạnh
d1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # AB
d2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5  # BC
d3 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5  # AC

# Kiểm tra tam giác cân
can = False
for d in [(d1, d2), (d1, d3), (d2, d3)]:
    if abs(d[0] - d[1]) < 1e-9:  # So sánh với sai số nhỏ
        can = True
        break

if can:
    print("Tam giác cân.")
else:
    print("Tam giác không cân.")
