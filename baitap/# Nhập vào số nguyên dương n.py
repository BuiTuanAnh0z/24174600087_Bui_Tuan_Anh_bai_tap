# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Kiểm tra điều kiện n > 0
if n <= 0:
    print("Giá trị của n phải lớn hơn 0")
else:
    # Tính tổng Σ(1/n^2) từ n=1 đến n
    sum_part = sum(1 / (i**2) for i in range(1, n+1))

    # Tính tích Π((-k)^3) từ k=1 đến n
    prod_part = 1
    for k in range(1, n+1):
        prod_part *= (-k)**3

    # Tính tổng S
    S = sum_part + prod_part

    # In kết quả
    print(f"Kết quả S = {S}")
