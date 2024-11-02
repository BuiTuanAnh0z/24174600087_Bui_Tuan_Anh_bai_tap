# Nhập vào n từ người dùng
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem số hoàn hảo có thể được tìm thấy
if n < 2:
    print("Không có số hoàn hảo nhỏ hơn", n)
else:
    print(f"Các số hoàn hảo nhỏ hơn {n} là:")
    
    # Duyệt qua các số từ 2 đến n-1
    for num in range(2, n):
        tong_cac_uoc_so = 0  # Tổng các ước số của num
        # Tính tổng các ước số của num
        for i in range(1, num):
            if num % i == 0:
                tong_cac_uoc_so += i
                
        # Kiểm tra nếu tổng các ước số bằng num
        if tong_cac_uoc_so == num:
            print(num)
