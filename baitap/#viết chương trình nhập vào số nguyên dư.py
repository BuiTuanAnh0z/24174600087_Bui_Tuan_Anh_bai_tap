#viết chương trình nhập vào số nguyên dương n, khi nào nhập vào số lẻ thì dừng chương trình 
for _ in range(1, 1000):  # Đặt một số lớn để đảm bảo vòng lặp có thể chạy nhiều lần
    n = int(input("Nhập vào một số nguyên dương: "))
    if n <= 0:
        print("Vui lòng nhập một số nguyên dương.")
        continue
    if n % 2 != 0:  # Kiểm tra nếu là số lẻ
        print("Bạn đã nhập số lẻ. Dừng chương trình.")
        break
    else:
        print(f"Bạn đã nhập số chẵn: {n}. Tiếp tục.")
